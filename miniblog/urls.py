from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import PostListView, AboutView
from django.views.generic import TemplateView
from .settings import base
urlpatterns = patterns('',
    url(r"^$", PostListView.as_view(),name="home"),
    url(r"^blog/", include("blog.urls", namespace="blog",app_name="blog")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': base.MEDIA_ROOT, 'show_indexes':True}),
    url(r"^about/$",AboutView.as_view(), name="about"),
    url(r"^contact/$",TemplateView.as_view(template_name='contact.html'),name="contact"),
    url(r"^markdown/",include("django_markdown.urls")),
)
