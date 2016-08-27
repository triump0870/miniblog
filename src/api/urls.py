from rest_framework.routers import DefaultRouter

from django.conf.urls import url, include

from api.views import PostViewSet, TagViewSet, UserViewSet, schema_view


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'tags', TagViewSet)
router.register(r'users', UserViewSet)


urlpatterns = router.urls
urlpatterns += url(r'^docs/', schema_view),