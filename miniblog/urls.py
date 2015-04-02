from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
urlpatterns = patterns('',
    url(r"^$", views.HomepageView.as_view(),name="home"),
    url(r"^add/post$",'blog.views.add_post'),
    url(r"^post/view$",'blog.views.view_post'),
    url(r"^accounts/login/$",'django.contrib.auth.views.login'),
    url(r"^blog/", include("blog.urls", namespace="blog",app_name="blog")),
    url(r'^admin/', include(admin.site.urls)),
)
