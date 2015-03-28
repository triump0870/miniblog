from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.
class PublishedPostMixin(object):
	def get_queryset(self):
		queryset = super(PublishedPostMixin, self).get_queryset()
		return queryset.filter(published=True)

class PostListView(PublishedPostMixin,ListView):
	model = Post

class PostDetailView(PublishedPostMixin,DetailView):
	model = Post
	