from django import forms
from .models import Post, Comment


# 게시글 폼
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['category','title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'write-title',
                'id': 'board-title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'write-content',
                'id': 'board-content'
            }) ,
            'category': forms.Select(attrs={
                'class': 'write-category',
                'id': 'category'
            })
        }
        


# 댓글 폼
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={    'class':'cm-write'})
        }


# 검색 폼
class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='search_Word')