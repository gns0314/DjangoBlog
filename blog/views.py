from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from .models import Post, Comment
from .forms import PostForm, CommentForm
# Create your views here.


class Index(View):
    def get(self, request):
        post_objs = Post.objects.all().order_by('-created_at')
        cnt = Post.objects.count()
        context = {
            'posts': post_objs,
            'cnt': cnt
        }
        return render(request, 'blog/post_list.html', context)
    

# 게시글 작성
class Write(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'blog/post_form.html', context)

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:list')
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html')


# 게시글 상세보기
class DetailView(View):
    def get(self, request, pk): 
        try:
            post = Post.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return render(request, 'blog/deleted_post.html')
        comments = Comment.objects.filter(post=post)
        comment_form = CommentForm()
        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
        }
        post.update_counter

        return render(request, 'blog/post_detail.html', context)
    

# 게시글 수정
class Update(View):
    def get(self, request, pk): 
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title': post.title, 'content': post.content, 'category': post.category})
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, pk):
        post = Post.objects.get(pk = pk)
        form = PostForm(request.POST, request.FILES ,instance=post)
        if form.is_valid():
            post.category = form.cleaned_data['category']
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)

        form.add_error(None,'폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        
    

# 게시글 삭제
class Delete(View):
    def post(self, request, pk): 
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')
    

# 게시글 검색
class Search(View):
    def get(self, request):
        search_word = request.GET.get('search_word')
        category = request.GET.get('category') 
        posts = Post.objects.all().order_by('created_at')
        sort = request.GET.get('sort', 'latest')

        if search_word:
            posts = posts.filter(Q(title__icontains=search_word) | Q(category__icontains=search_word))

        if category:
            posts = posts.filter(category=category)

        if sort == 'hits':
            posts = posts.order_by('-hit')  
        else:
            posts = posts.order_by('-created_at')  

        context = {
            'posts': posts,
            'search_word': search_word,
            'category': category,
            'sort': sort  
        }
        return render(request, 'blog/post_search.html', context)
    

# 댓글 작성
class CommentWrite(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)
        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user
            comment = Comment.objects.create(post=post, content=content, writer=writer)
            return redirect('blog:detail', pk=pk)

        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'comment_form': form
        }
        return render(request, 'blog/post_detail.html', context)
    

# 댓글 삭제
class CommentDelete(View):
    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        post_id = comment.post.id
        comment.delete()

        return redirect('blog:detail', pk = post_id)