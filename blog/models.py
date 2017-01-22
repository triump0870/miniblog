import uuid
from logging import getLogger
from time import time
from datetime import datetime
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import FileField
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify
from django.utils.deconstruct import deconstructible
from django_markdown.models import MarkdownField

User = settings.AUTH_USER_MODEL
logger = getLogger("blog")

# Choices
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

choice = (
    (1, 'Native Speaker'),
    (2, 'Professional Proficiency'),
    (3, 'Learner'),
)

star_choice = (
    ('x', '1'),
    ('xx', '2'),
    ('xxxx', '4'),
    ('xxxxx', '5'),
)

LOCAL_APPS = [
    'blog',
]


@deconstructible
class generatefilename(object):
    ''' Generates filename based on the time of upload'''

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        if self.path == "resume/":
            filename = "RohanRoy.pdf"
            return self.path + filename
        ext = filename.split('.')[-1]
        prefix = '-%s.%s' % (uuid.uuid4(), ext)
        return self.path + str(int(time())) + prefix


about_filename = generatefilename("images/")
postlist_filename = generatefilename("postlist/")
contact_filename = generatefilename("contact/")
post_filename = generatefilename("posts/")
projectlist_filename = generatefilename("projectlist/")
project_filename = generatefilename("projectlist/projects/")
side_filename = generatefilename("projects/side/")
user_filename = generatefilename("avatar/")
resume_filename = generatefilename("resume/")


# def about_filename()
class CustomManager(models.Manager):
    def get_queryset(self):
        return super(CustomManager, self).get_queryset().filter(status='p')


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = self.slug.lower()
        super(Tag, self).save(*args, **kwargs)


# Model classes in lexicographic order

class About(models.Model):
    content = MarkdownField()

    def __str__(self):
        return str(self.pk)


class Conference(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=100)
    link = models.URLField('Link', blank=True, null=True)
    date = models.DateField(editable=True, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+919999999990'. Up to 15 digits allowed.")
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=70, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=10, validators=[phone_regex])
    message = models.TextField()

    def __str__(self):
        return str(self.pk)


class Education(models.Model):
    course = models.CharField(max_length=30)
    institution = models.CharField(max_length=50)
    website = models.URLField('URL', max_length=255, blank=True)
    start_date = models.DateField(editable=True)
    end_date = models.DateField(editable=True, blank=True, null=True)
    mode = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.course

    def is_present(self):
        if not self.end_date:
            return 'Present'
        else:
            return self.end_date.year


class Image(models.Model):
    about_image = models.ImageField(upload_to=about_filename, blank=True, null=True)
    postlist_image = models.ImageField(upload_to=postlist_filename, blank=True, null=True)
    contact_image = models.ImageField(upload_to=contact_filename, blank=True, null=True)
    projectlist_image = models.ImageField(upload_to=projectlist_filename, blank=True, null=True)

    def __str__(self):
        return str(self.pk)


class Language(models.Model):
    language = models.CharField(max_length=70)
    proficiency = models.IntegerField(choices=choice, default=1)
    star = models.CharField(max_length=5, choices=star_choice, default='xxx')

    def __str__(self):
        return self.language


class Music(models.Model):
    music = models.CharField(max_length=255)
    url = models.URLField('Music_URL', null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.music


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = MarkdownField()
    image = models.ImageField('Cover Image', upload_to=post_filename, blank=True, null=True)
    author = models.ForeignKey(User, related_name="posts")
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    objects = CustomManager()

    class Meta:
        ordering = ["-created_at", "title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return "blog:detail", (), {'slug': self.slug}


class Project(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = MarkdownField()
    image = models.ImageField(upload_to=project_filename, blank=True, null=True)
    side_image = models.ImageField(upload_to=side_filename, blank=True, null=True)
    date = models.DateField(editable=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    slug = models.SlugField(max_length=255, unique=True)
    url = models.URLField('URL', max_length=255, blank=True)
    github = models.URLField('GITHUB_URL', max_length=255, blank=True)
    objects = CustomManager()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("projectdetail", (), {'slug': self.slug})


class Skill(models.Model):
    name = models.CharField(max_length=30)
    stage = models.CharField(max_length=15)
    rating = models.IntegerField(default=0)
    info = models.TextField()

    def __str__(self):
        return self.name


class UserData(models.Model):
    fullname = models.CharField(max_length=255)
    user = models.CharField(max_length=70, unique=True, blank=False, null=False)
    avatar = models.ImageField(upload_to=user_filename, blank=True, null=True)
    border_color = models.CharField(max_length=10, blank=True, null=True)
    border_width = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    contact = models.EmailField(max_length=70, blank=True, null=True)
    website = models.URLField('Website', blank=True, null=True)
    linkedin = models.URLField('LinkedIn', blank=True, null=True)
    facebook = models.URLField('Facebook', blank=True, null=True)
    twitter = models.URLField('Twitter', blank=True, null=True)
    googleplus = models.URLField('Google+', blank=True, null=True)
    github = models.URLField('Github', blank=True, null=True)
    hackernews = models.URLField('HackerNews', blank=True, null=True)
    email = models.EmailField(max_length=70, unique=True, blank=False, null=False)
    resume = models.FileField(upload_to="resume/rohanroy.pdf", blank=True, null=True)

    def __str__(self):
        return self.user


class Work(models.Model):
    company = models.CharField(max_length=255)
    website = models.URLField(blank=False, null=False)
    designation = models.CharField(max_length=30)
    content = MarkdownField()
    start_date = models.DateField(editable=True)
    end_date = models.DateField(editable=True, null=True, blank=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.designation

    def span(self):
        months = lambda a, b: abs((a.year - b.year) * 12 + a.month - b.month) + int(abs(a.day - b.day) > 15)
        if self.end_date:
            diff = months(self.end_date, self.start_date)
            if diff > 1:
                diff = str(diff) + ' Months'
            else:
                diff = str(diff) + ' Month'
        else:
            diff = months(datetime.now(), self.start_date)
            diff = str(diff) + " Months - Present"
        logger.info("Diff is: [{}]".format(diff))
        return diff


def delete_files(files_list):
    for file_ in files_list:
        if file_ and hasattr(file_, 'storage') and hasattr(file_, 'name'):
            # this accounts for different file storages (e.g. when using django-storages)
            storage_, name_ = file_.storage, file_.name
            storage_.delete(name_)


@receiver(post_delete)
def handle_files_on_delete(sender, instance, **kwargs):
    # presumably you want this behavior only for your apps, in which case you will have to specify them
    is_valid_app = sender._meta.app_label in LOCAL_APPS
    if is_valid_app:
        delete_files(
            [getattr(instance, field_.name, None) for field_ in sender._meta.fields if isinstance(field_, FileField)])


@receiver(pre_save)
def set_instance_cache(sender, instance, **kwargs):
    # prevent errors when loading files from fixtures
    from_fixture = 'raw' in kwargs and kwargs['raw']
    is_valid_app = sender._meta.app_label in LOCAL_APPS
    if is_valid_app and not from_fixture:
        # retrieve the old instance from the database to get old file values
        # for Django 1.8+, you can use the *refresh_from_db* method
        old_instance = sender.objects.filter(pk=instance.id).first()
        if old_instance is not None:
            # for each FileField, we will keep the original value inside an ephemeral `cache`
            instance.files_cache = {
                field_.name: getattr(old_instance, field_.name, None) for field_ in sender._meta.fields if
                isinstance(field_, FileField)
                }


@receiver(post_save)
def handle_files_on_update(sender, instance, **kwargs):
    if hasattr(instance, 'files_cache') and instance.files_cache:
        deletables = []
        for field_name in instance.files_cache:
            old_file_value = instance.files_cache[field_name]
            new_file_value = getattr(instance, field_name, None)
            # only delete the files that have changed
            if old_file_value and old_file_value != new_file_value:
                deletables.append(old_file_value)
        delete_files(deletables)
        instance.files_cache = {field_name: getattr(instance, field_name, None) for field_name in instance.files_cache}
