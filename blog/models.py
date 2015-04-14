from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from vote.managers import VotableManager
from django_markdown.models import MarkdownField
# Create your models here.

class PostManager(models.Manager):
	def live(self):
		return self.model.objects.filter(published=True)

class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)#save the timestamp when the model first creatred and not the field is editable in admin
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255,blank=True,default='') #blank = True i.e it is not required for validatipn purpose , default = '' for not slug provided
	content = MarkdownField()
	published = models.BooleanField(default=True)
	author = models.ForeignKey(User, related_name="posts")
	rank_score = models.FloatField(default=0.0)
	url = models.URLField('URL',max_length=250, blank=True)
	# love = models.PositiveIntegerField(default=0)
	objects = PostManager()
	votes = VotableManager()
	class Meta:
		ordering = ["-created_at", "title"]
		
	def __unicode__(self):
		return self.title

	def save(self, *args, ** kwargs):
		if not self.slug:
			self.slug = slugify(self.title) #title become the slug
		super(Post, self).save(*args,**kwargs)
	
	@models.permalink
	def get_absolute_url(self):
		return ("blog:detail",(),{'slug':self.slug
							})
class Comments(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=75)
	text = models.TextField()
	post = models.ForeignKey(Post)
	# love = models.PositiveIntegerField(default=0)
	commented_at = models.DateTimeField(auto_now_add=True, editable=False)

	class Meta:
		ordering = ["-commented_at","email"]
	def __unicode__(self):
		return self.text

class Vote(models.Model):
	voter = models.ForeignKey(User)
	link = models.ForeignKey(Post)

	def __unicode__(self):
		return "%s upvoted %s"%(self.voter.username, self.link.title)
# class Like(models.Model):
# 	like_post = models.ForeignKey(Post)
# 	liked_on = models.DateTimeField(auto_now_add=True)
	
# class Hit(models.Model):
# 	date = models.DateTimeField(auto_now=True)
# 	content_type = models.ForeignKey(ContentType)
# 	object_id = models.PositiveIntegerField()
# 	content_object = generic.GenericForeignKey('content_type','object_id')
# 	ip = models.CharField(max_length=40)
# 	session = models.CharField(max_length=40)
