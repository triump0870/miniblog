#All the imports
from .models import Post
from django.views.generic import ListView, DetailView
<<<<<<< HEAD

=======
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from forms import PostForm, CommentForm
>>>>>>> 9d76e85f60f79987544f8576b566f06f1d65f93d
# Create your views here.

@user_passes_test(lambda u:u.is_superuser)
def add_post(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.author = request.user
		post.save()
		return redirect(post)
	return render_to_response('blog/add_post.html',{'form':form},context_instance=RequestContext(request))

def view_post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	form = CommentForm(request.POST or None)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.post = post
		comment.save()
		request.session['name'] = comment.name
		request.session['email'] = comment.email
		request.session['website'] = comment.website
		return redirect(request.path)
	form.initial['name'] = request.session.get('name')
	form.initial['email'] = request.session.get('email')
	form.initial['website'] = request.session.get('website')
	return render_to_response('blog/blog_post.html',
		{
			'post':post,
			'form':form,
		},
		context_instance=RequestContext(request))


class PublishedPostMixin(object):
	def get_queryset(self):
		return self.model.objects.live()

class PostListView(PublishedPostMixin,ListView):
	model = Post

class PostDetailView(PublishedPostMixin,DetailView):
	model = Post
<<<<<<< HEAD
	
=======
	# template_name = 'blog_post.html'
	# form = CommentForm(request.POST or None)
	# if form.is_valid():
	# 	comment = form.save(commit=False)
	# 	comment.post = post
	# 	comment.save()
	# 	request.session['name'] = comment.name
	# 	request.session['email'] = comment.email
	# 	request.session['website'] = comment.website
	# form.initial['name'] = request.session.get('name')
	# form.initial['email'] = request.session.get['email']
	# form.initial['website'] = request.session.get['website']
>>>>>>> 9d76e85f60f79987544f8576b566f06f1d65f93d
