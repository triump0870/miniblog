from rest_framework import serializers
from blog.models import Post, Tag


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