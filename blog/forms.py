from django import forms
from models import Post, Comments

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['author','slug']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		exclude = ['post']
