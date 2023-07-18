from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, PostSearchForm
from django.db.models import Q
# Create your views here.


class Index(View):
    def get(self, request):
        post_objs = Post.objects.all()
        context = {
            'posts': post_objs,
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
        form = PostForm(request.POST)
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
        post = Post.objects.get(pk = pk)
        context = {
            'post': post
        }

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
        form = PostForm(request.POST)
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
        return render(request, 'blog/form_error.html', context)
    

# 게시글 삭제
class Delete(View):
    def post(self, request, pk): 
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')
    

# 게시글 검색
class Search(View):
    def post(self, request):
        search_word = request.POST.get('search_word', '')
        posts = Post.objects.filter(Q(title__icontains=search_word) | Q(category__icontains=search_word))
        context = {
            'posts': posts
        }
        return render(request, 'blog/post_search.html', context)
    

