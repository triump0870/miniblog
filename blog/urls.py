from django.conf.urls import patterns, url
from blog.views import  PostListView, vote, BlogListView, view_post, about_page, TagListView
from . import feed
urlpatterns = patterns('',
	url(r"^$",BlogListView.as_view(), name="list"),
	url(r"^tag/(?P<slug>[\w-]+)/$",TagListView.as_view(), name="tag"),
	url(r"^(?P<slug>[\w-]+)/$",view_post, name="detail"),
	url(r"^(?P<post_id>[0-9]+)/vote/$",vote, name='vote'),
	url(r"^feed/$",feed.LatestPosts(), name='feed'),
	
	)