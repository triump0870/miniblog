from django.shortcuts import render
from .models import Post
# Create your views here.
def blog_list( request, *args, **kwargs):
	post_list = Post.objects.filter(published=True)
	template_name = "blog/post_list.html"

	context = {
		"post_list": post_list
	}

	return render(request, template_name, context)
def blog_detail(request,pk,*args,**kwargs):
	post = Post.objects.get(pk=pk, published=True)
	template_name = 'blog/post_detail.html'
	context = {
		'post':post
	}
	return render(request,template_name,context)