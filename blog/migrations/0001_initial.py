# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models
import blog.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('content', django_markdown.models.MarkdownField()),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=100)),
                ('link', models.URLField(verbose_name='Link', null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('status', models.CharField(max_length=1, choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')])),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+919999999990'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=30)),
                ('institution', models.CharField(max_length=50)),
                ('website', models.URLField(verbose_name='URL', max_length=255, blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('mode', models.CharField(max_length=20, blank=True)),
                ('status', models.CharField(max_length=1, choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')])),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('about_image', models.ImageField(upload_to=blog.models.generatefilename('images/'), null=True, blank=True)),
                ('postlist_image', models.ImageField(upload_to=blog.models.generatefilename('postlist/'), null=True, blank=True)),
                ('contact_image', models.ImageField(upload_to=blog.models.generatefilename('contact/'), null=True, blank=True)),
                ('projectlist_image', models.ImageField(upload_to=blog.models.generatefilename('projectlist/'), null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=70)),
                ('proficiency', models.IntegerField(choices=[(1, 'Native Speaker'), (2, 'Professional Proficiency'), (3, 'Learner')], default=1)),
                ('star', models.CharField(max_length=5, choices=[('x', '1'), ('xx', '2'), ('xxxx', '4'), ('xxxxx', '5')], default='xxx')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('music', models.CharField(max_length=255)),
                ('url', models.URLField(verbose_name='Music_URL')),
                ('status', models.CharField(max_length=1, choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('content', django_markdown.models.MarkdownField()),
                ('image', models.ImageField(verbose_name='Cover Image', upload_to=blog.models.generatefilename('posts/'), null=True, blank=True)),
                ('status', models.CharField(max_length=1, choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='p')),
                ('author', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255, null=True, blank=True)),
                ('content', django_markdown.models.MarkdownField()),
                ('image', models.ImageField(upload_to=blog.models.generatefilename('projectlist/projects/'), null=True, blank=True)),
                ('side_image', models.ImageField(upload_to=blog.models.generatefilename('projects/side/'), null=True, blank=True)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=1, choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='p')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('url', models.URLField(verbose_name='URL', max_length=255, blank=True)),
                ('github', models.URLField(verbose_name='GITHUB_URL', max_length=255, blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('stage', models.CharField(max_length=15)),
                ('rating', models.IntegerField(default=0)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=70, unique=True)),
                ('avatar', models.ImageField(upload_to=blog.models.generatefilename('avatar/'), null=True, blank=True)),
                ('border_color', models.CharField(max_length=10, null=True, blank=True)),
                ('border_width', models.IntegerField(null=True, blank=True)),
                ('role', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('contact', models.EmailField(max_length=70, null=True, blank=True)),
                ('website', models.URLField(verbose_name='Website', null=True, blank=True)),
                ('linkedin', models.URLField(verbose_name='LinkedIn', null=True, blank=True)),
                ('facebook', models.URLField(verbose_name='Facebook', null=True, blank=True)),
                ('twitter', models.URLField(verbose_name='Twitter', null=True, blank=True)),
                ('googleplus', models.URLField(verbose_name='Google+', null=True, blank=True)),
                ('github', models.URLField(verbose_name='Github', null=True, blank=True)),
                ('hackernews', models.URLField(verbose_name='HackerNews', null=True, blank=True)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('resume', models.FileField(upload_to=blog.models.generatefilename('resume/'), null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=255)),
                ('website', models.URLField()),
                ('designation', models.CharField(max_length=30)),
                ('content', django_markdown.models.MarkdownField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
