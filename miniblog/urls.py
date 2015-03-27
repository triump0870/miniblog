from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import blog_list, blog_detail
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^blog/$",blog_list,name='blog_list'),
    url(r"^blog/(?P<pk>\d+)/$",blog_detail,name='blog_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
