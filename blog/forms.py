from django import forms
from models import Post, Comments

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['author','slug']
		# widget = {
		# 	'name':forms.TextInput(attrs={'placeholder':'Enter Name'}),
		# 	'website':forms.URLInput(attrs={'placeholder':'Enter Your Website'}),
		# }
	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs\
		.update({
			'placeholder': 'Name'
			})

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		exclude = ['post']
