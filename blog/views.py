#All the imports
from .models import Post, Comment, Vote
from django.views.generic import ListView, DetailView, TemplateView
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from forms import PostForm, CommentForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
		return redirect(request.path)
	# form.initial['name'] = request.session.get('name')
	# form.initial['email'] = request.session.get('email')
	# form.initial['website'] = request.session.get('website')
	return render_to_response('blog/blog_post.html',
		{
			'post':post,
			'form':form,
		},
		context_instance=RequestContext(request))

# def like(request, post_id):
# 	new_like= Like.objects.get(post_id=post_id)
# 	new_like.like += 1
# 	new_like.save()
# 	return 
def about_page(request):
    template_name = "about.html"
    return render_to_response(template_name, context_instance=RequestContext(request))

def vote(request, post_id):
	return HttpResponse("You're voting on post %s."%post_id)
	
class PublishedPostMixin(object):
	def get_queryset(self):
		return self.model.objects.live()

class PostListView(PublishedPostMixin,ListView):
	model = Post
	template_name = "index.html"

class BlogListView(ListView):
	model = Post
	queryset = Post.objects.all().filter(published=True)
	paginate_by = 2

	

class PostDetailView(PublishedPostMixin,DetailView):
	model = Post