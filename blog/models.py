from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
# Create your models here.

class PostManager(models.Manager):
	def live(self):
		return self.model.objects.filter(published=True)

class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)#save the timestamp when the model first creatred and not the field is editable in admin
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255,blank=True,default='') #blank = True i.e it is not required for validatipn purpose , default = '' for not slug provided
	content = models.TextField()
	published = models.BooleanField(default=True)
	author = models.ForeignKey(User, related_name="posts")
	objects = PostManager()
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
	website = models.URLField(max_length=200, null=True, blank=True)
	email = models.EmailField(max_length=75)
	text = models.TextField()
	post = models.ForeignKey(Post)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)

	def __unicode__(self):
		return self.text
