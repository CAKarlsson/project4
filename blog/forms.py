from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    """
        Form for post submission
    """
    class Meta:
        """
        Metadata for post form
        """
        model = Post
        fields = ['title', 'content']
        labels = {'title': 'Title', 'content': 'Post Content'}