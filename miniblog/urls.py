from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views import IndexView, AboutView, ContactView, ProjectListView, ProjectDetailView

# registering admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r"^$", IndexView.as_view(), name="home"),
                       # url(r'^ajax-upload/', include('startproject.cicu.urls')),
                       url(r"^blog/", include("blog.urls", namespace="blog", app_name="blog")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                       url(r"^about/$", AboutView.as_view(), name="about"),
                       url(r"^contact/$", ContactView.as_view(), name="contact"),
                       url(r"^markdown/", include("django_markdown.urls")),
                       url(r"^projects/$", ProjectListView.as_view(), name="project"),
                       url(r"^projects/(?P<slug>[\w-]+)/$", ProjectDetailView.as_view(), name="projectdetail"),
                       )

urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
                        )

urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                        )
