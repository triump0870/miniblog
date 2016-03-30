from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, TagViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = router.urls
urlpatterns += url(r'^docs/', include('rest_framework_swagger.urls')),