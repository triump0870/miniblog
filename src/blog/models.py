from __future__ import absolute_import

import os
from markdownx.models import MarkdownxField

from django.conf import settings
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from miniblog.filename import generatefilename

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
	title = models.CharField(max_length=180)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ["title"]

	def __unicode__(self):
		return self.slug

	@models.permalink
	def get_absolute_url(self):
		return ("blog:tag", None, {"slug": self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)
	content = MarkdownxField()
	image = models.ImageField(
    'Cover Image',
    upload_to=post_filename,
    blank=True,
     null=True)
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
		super(Post, self).save(*args, **kwargs)

	@models.permalink
	def get_absolute_url(self):
		return ("blog:detail", (), {'slug': self.slug})


@receiver(post_delete, sender=Post)
def auto_delete_image_on_delete(sender, instance, **kwargs):
	"""
	Deletes image from filesystem when corresponding `Post` object is deleted.
    """
	if instance.image:
		if os.path.isfile(instance.image.path):
			os.remove(instance.image.path)


@receiver(pre_save, sender=Post)
def auto_delete_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
    	return False

    try:
    	old_image = Post.objects.get(pk=instance.pk).image
    except Post.DoesNotExist:
    	return False

    new_image = instance.image
    if not old_image == new_image:
    	if old_image:
	    	if os.path.isfile(old_image.path):
	    		os.remove(old_image.path)
