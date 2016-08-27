from rest_framework import serializers
from blog.models import Post, Tag
from django.contrib.auth import get_user_model

User = get_user_model()


class TagSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='api:tag-detail')
	class Meta:
		model = Tag
		fields = ('url','slug',)

class PostSerializer(serializers.ModelSerializer):
	tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(),source='tags', many=True)
	class Meta:
		model = Post
		fields = ('title','content', 'image', 'author', 'updated_at','tag')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
	class Meta:
		model = User
		fields = ('url','email', 'name')
		read_only_fields = ('email',)