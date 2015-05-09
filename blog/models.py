from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django_markdown.models import MarkdownField
from django.db.models import TextField, Count
# from time import time
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.
def generate_filename(instance, filename):
	ext = filename.split('.')[-1]
	return 'images/'+str(int(time()))+'.'+ext

class PostManager(models.Manager):
	def live(self):
		return self.model.objects.filter(published=True)

class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __unicode__(self):
		return self.slug

	def save(self, *args, **kwargs):
		if self.slug:
			self.slug = self.slug.lower()
		super(Tag, self).save(*args, **kwargs)

class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255,unique=True)
	content = MarkdownField()
	author = models.ForeignKey(User, related_name="posts")
	url = models.URLField('URL',max_length=250, blank=True)
	tags = models.ManyToManyField(Tag)
	published = models.BooleanField(default=True)
	objects = PostManager()
	
	class Meta:
		ordering = ["-created_at", "title"]
		
	def __unicode__(self):
		return self.title

	def save(self, *args, ** kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Post, self).save(*args,**kwargs)
	
	@models.permalink
	def get_absolute_url(self):
		return ("blog:detail",(),{'slug':self.slug})

class Project(models.Model):
	title = models.CharField(max_length=255)
	subtitle = models.CharField(max_length=255, blank=True,null=True)
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
	website = models.URLField(blank=False, null=False)
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

class About(models.Model):
	content = MarkdownField()

class Skill(models.Model):
	name = models.CharField(max_length=30)
	stage = models.CharField(max_length=15)
	rating = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Education(models.Model):
	course = models.CharField(max_length=30)
	institution = models.CharField(max_length=50)
	website = models.URLField('URL',max_length=255,blank=True)
	start_date = models.DateField(editable=True)
	end_date = models.DateField(editable=True,blank=True,null=True)
	mode = models.CharField(max_length=20, blank=True)
	published = models.BooleanField(default=True)

	class Meta:
		ordering = ['-start_date']
	def __unicode__(self):
		return self.course

	def is_present(self):
		if not self.end_date:
			return 'Present'
		else:
			return self.end_date.year

class Music(models.Model):
	music = models.CharField(max_length=255)
	url = models.URLField('Music_URL',null=False,blank=False)
	published = models.BooleanField(default=True)

	def __unicode__(self):
		return self.music

class UserData(models.Model):
	fullname = models.CharField(max_length=255)
	user = models.CharField(max_length=70, unique=True, blank=False, null=False)
	role = models.CharField(max_length=30)
	location = models.CharField(max_length=100)
	contact =  models.EmailField(max_length=70, blank=True, null=True)
	website = models.URLField('Website',blank=True, null=True)
	linkedin = models.URLField('LinkedIn',blank=True, null=True)
	facebook = models.URLField('Facebook',blank=True,null=True)
	twitter = models.URLField('Twitter',blank=True,null=True)
	googleplus = models.URLField('Google+',blank=True,null=True)
	github = models.URLField('Github',blank=True,null=True)
	hackernews = models.URLField('HackerNews',blank=True,null=True)
	email = models.EmailField(max_length=70,unique=True, blank=False, null=False)
	testimonial = models.TextField()
	testimonial_name = models.CharField(max_length=255)
	testimonial_desig = models.CharField(max_length=70)
	testimonial_link = models.URLField('LinkedIn',blank=True,null=True)

	def __unicode__(self):
		return self.user

class Language(models.Model):
	choice = (
		(1,'Native Speaker'),
		(2,'Professional Proficiency'),
		(3,'Learner'),
		)
	star_choice = (
		('x','1'),
		('xx','2'),
		('xxx','3'),
		('xxxx','4'),
		('xxxxx','5'),
		)
	language = models.CharField(max_length=70)
	proficiency = models.IntegerField(max_length=1, choices=choice, default=1)
	star = models.CharField(max_length=5,choices=star_choice, default='xxx')

	def __unicode__(self):
		return self.language

class Conference(models.Model):
	name = models.CharField(max_length=255)
	place = models.CharField(max_length=100)
	link = models.URLField('Link', blank=True, null=True)
	date = models.DateField(editable=True, blank=True, null=True)
	published = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name


@receiver(post_delete, sender=Post)
def image_post_delete_handler(sender, **kwargs):
	Post = kwargs['instance']
	storage, path = Post.image.storage, Post.image.path
	storage.delete(path)
