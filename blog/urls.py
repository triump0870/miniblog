from django.conf.urls import patterns, url
from . import views
from blog.views import view_post
urlpatterns = patterns('',
	url(r"^$",views.PostListView.as_view(), name="list"),

	url(r"^(?P<slug>[\w-]+)/$",view_post, name="detail"),
	url(r"^(?P<post_id>[0-9]+)/vote/$",views.vote, name='vote'),
	)