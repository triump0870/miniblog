from django.shortcuts import render
from rest_framework import viewsets
from blog.models import Post, Tag
from api.serializers import PostSerializer, TagSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer