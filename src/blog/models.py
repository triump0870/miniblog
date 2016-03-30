from django.db import models
from myblog.filename import generatefilename

from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.conf import settings

from markdownx.models import MarkdownxField

# User model
User = settings.AUTH_USER_MODEL

# Choices
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

# Random filename creator
post_filename = generatefilename("posts/")

# Custom manager
class CustomManager(models.Manager):
	def get_queryset(self):
		return super(CustomManager, self).get_queryset().filter(status='p')

# Create your models here.
class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __unicode__(self):
		return self.slug

	def save(self, *args, **kwargs):
		if self.slug:
			self.slug = self.slug.lower()
		super(Tag, self).save(*args, **kwargs)

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255,unique=True)
	content = MarkdownxField()
	image = models.ImageField('Cover Image',upload_to=post_filename, blank=True, null=True)
	author = models.ForeignKey(User, related_name="posts")
	tags = models.ManyToManyField(Tag)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	
	objects = CustomManager()

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

@receiver(post_delete, sender=Post)
def image_post_delete_handler(sender,instance, **kwargs):
	instance.image.deleted(save=False)
