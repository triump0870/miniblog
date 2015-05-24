from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import IndexView, AboutView, ContactView
from django.views.generic import TemplateView
from .settings import base
#registering admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r"^$", IndexView.as_view(),name="home"),
    # url(r'^ajax-upload/', include('startproject.cicu.urls')),
    url(r"^blog/", include("blog.urls", namespace="blog",app_name="blog")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': base.MEDIA_ROOT, 'show_indexes':True}),
    url(r"^about/$",AboutView.as_view(), name="about"),
    url(r"^contact/$",ContactView.as_view(), name="contact"),
    url(r"^markdown/",include("django_markdown.urls")),
)
