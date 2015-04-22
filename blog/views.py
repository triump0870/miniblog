#All the imports
from .models import Post,  Vote, Project, Work, Tag, About
from django.views.generic import ListView, DetailView, TemplateView
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from forms import PostForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class PublishedPostMixin(object):
	def get_queryset(self):
		return self.model.objects.live()

class PostListView(PublishedPostMixin,ListView):
	model = Post
	template_name = "index.html"
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(PostListView, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		last = Project.objects.reverse()[0]
		context['project_list'] = Project.objects.all()[:last.id]
		context['work_list'] = Work.objects.all()
		context['lastest'] = last
		context['about_list'] = About.objects.all()[:3]
		return context

class BlogListView(ListView):
	model = Post
	queryset = Post.objects.all().filter(published=True)
	paginate_by = 5

class TagListView(ListView):
	models = Tag
	paginate_by = 5
	template_name = 'blog/post_list.html'

	def get_queryset(self):
		slug = self.kwargs['slug']
		tag = Tag.objects.get(slug=slug)
		results = Post.objects.filter(tags=tag)
		return results

class PostDetailView(PublishedPostMixin,DetailView):
	model = Post
	template_name = "blog/blog_post.html"

class AboutView(ListView):
	model = About
	template_name = "about.html"

def vote(request, post_id):
	return HttpResponse("You're voting on post %s."%post_id)
	