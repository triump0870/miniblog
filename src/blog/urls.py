from blog.views import PostListView, TagListView, PostDetailView
from django.conf.urls import url

from . import feed

urlpatterns = [
    url(r"^$", PostListView.as_view(), name="list"),
    url(r"^tag/(?P<slug>[\w-]+)/$", TagListView.as_view(), name="tag"),
    url(r"^(?P<slug>[\w-]+)/$", PostDetailView.as_view(), name="detail"),
    url(r"^feed/$", feed.LatestPosts(), name='feed'),
]
