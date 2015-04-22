from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from vote.managers import VotableManager
from django_markdown.models import MarkdownField
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField, Count
from time import time
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.
def generate_filename(instance, filename):
	ext = filename.split('.')[-1]
	return 'images/'+str(int(time()))+'.'+ext

class PostManager(models.Manager):
	def live(self):
		return self.model.objects.filter(published=True)

class PostVoteCountManager(models.Manager):
	def get_queryset(self):
		return super(PostVoteCountManager, self).get_queryset().annotate(
			votes = Count('vote')
			).order_by("-votes")

class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __unicode__(self):
		return self.slug

	def save(self, *args, **kwargs):
		if self.slug:
			self.slug = self.slug.lower()
		super(Tag, self).save(*args, **kwargs)

class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)#save the timestamp when the model first creatred and not the field is editable in admin
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255,unique=True) #blank = True i.e it is not required for validatipn purpose , default = '' for not slug provided
	content = MarkdownField()
	published = models.BooleanField(default=True)
	author = models.ForeignKey(User, related_name="posts")
	rank_score = models.FloatField(default=0.0)
	url = models.URLField('URL',max_length=250, blank=True)
	tags = models.ManyToManyField(Tag)
	image = models.ImageField(upload_to=generate_filename,null=True, blank=True)
	with_votes = PostVoteCountManager()
	objects = PostManager()
	formfield_overrides = {TextField: {'widget':AdminMarkdownWidget}}
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
# class Comment(models.Model):
# 	name = models.CharField(max_length=50)
# 	email = models.EmailField(max_length=75)
# 	text = models.TextField()
# 	post = models.ForeignKey(Post)
# 	# love = models.PositiveIntegerField(default=0)
# 	commented_at = models.DateTimeField(auto_now_add=True, editable=False)

# 	class Meta:
# 		ordering = ["-commented_at","email"]
		
# 	def __unicode__(self):
# 		return self.text

class Vote(models.Model):
	voter = models.ForeignKey(User)
	link = models.ForeignKey(Post)

	def __unicode__(self):
		return "%s upvoted %s"%(self.voter.username, self.link.title)

class Project(models.Model):
	title = models.CharField(max_length=255)
	content = MarkdownField()
	image = models.ImageField(upload_to=generate_filename, blank=True, null=True)
	date = models.DateField(editable=True)
	published = models.BooleanField(default=True)
	slug = models.SlugField(max_length=255, unique=True)
	url = models.URLField('URL',max_length=255,blank=True)
	github = models.URLField('GITHUB_URL',max_length=255,blank=True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Project, self).save(*args, **kwargs)

class Work(models.Model):
	company = models.CharField(max_length=255)
	designation = models.CharField(max_length=30)
	content = MarkdownField()
	start_date = models.DateField(editable=True)
	end_date = models.DateField(editable=True,null=True,blank=True)
	class Meta:
		ordering = ["-start_date"]

	def __unicode__(self):
		return self.designation

	def span(self):
		if self.end_date:
			months = lambda a, b: abs((a.year - b.year) * 12 + a.month - b.month) + int(abs(a.day - b.day) > 15)
			diff = months(self.end_date,self.start_date)
			if diff > 1:
				diff = str(diff)+' Months'
			else:
				diff = str(diff)+' Month'
		else:
			diff = 'Present'
		return diff

@receiver(post_delete, sender=Post)
def image_post_delete_handler(sender, **kwargs):
	Post = kwargs['instance']
	storage, path = Post.image.storage, Post.image.path
	storage.delete(path)
