from django.conf.urls import patterns, url
from blog.views import view_post, PostListView, vote
urlpatterns = patterns('',
	url(r"^$",PostListView.as_view(), name="list"),

	url(r"^(?P<slug>[\w-]+)/$",view_post, name="detail"),
	url(r"^(?P<post_id>[0-9]+)/vote/$",vote, name='vote'),
	)