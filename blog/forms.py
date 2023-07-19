from django import forms
from .models import Post, Comment


# 게시글 폼
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['category','title', 'content']


# 댓글 폼
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': '5', 'cols': '20'})
        }


# 검색 폼
class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='search_Word')