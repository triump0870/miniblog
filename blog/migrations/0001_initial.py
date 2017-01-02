# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models
from django.conf import settings
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('content', django_markdown.models.MarkdownField()),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=100)),
                ('link', models.URLField(verbose_name='Link', blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(unique=True, max_length=70)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('course', models.CharField(max_length=30)),
                ('institution', models.CharField(max_length=50)),
                ('website', models.URLField(verbose_name='URL', blank=True, max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('mode', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('about_image', models.ImageField(blank=True, null=True, upload_to=blog.models.generatefilename('images/'))),
                ('postlist_image', models.ImageField(blank=True, null=True, upload_to=blog.models.generatefilename('postlist/'))),
                ('contact_image', models.ImageField(blank=True, null=True, upload_to=blog.models.generatefilename('contact/'))),
                ('projectlist_image', models.ImageField(blank=True, null=True, upload_to=blog.models.generatefilename('projectlist/'))),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('language', models.CharField(max_length=70)),
                ('proficiency', models.IntegerField(default=1, choices=[(1, 'Native Speaker'), (2, 'Professional Proficiency'), (3, 'Learner')])),
                ('star', models.CharField(choices=[('x', '1'), ('xx', '2'), ('xxxx', '4'), ('xxxxx', '5')], default='xxx', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('music', models.CharField(max_length=255)),
                ('url', models.URLField(verbose_name='Music_URL')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('content', django_markdown.models.MarkdownField()),
                ('image', models.ImageField(verbose_name='Cover Image', blank=True, null=True, upload_to=blog.models.generatefilename('posts/'))),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='p', max_length=1)),
                ('author', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, null=True, max_length=255)),
                ('content', django_markdown.models.MarkdownField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.generatefilename('projectlist/projects/'))),
                ('side_image', models.ImageField(blank=True, null=True, upload_to=blog.models.generatefilename('projects/side/'))),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='p', max_length=1)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('url', models.URLField(verbose_name='URL', blank=True, max_length=255)),
                ('github', models.URLField(verbose_name='GITHUB_URL', blank=True, max_length=255)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('stage', models.CharField(max_length=15)),
                ('rating', models.IntegerField(default=0)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('user', models.CharField(unique=True, max_length=70)),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.generatefilename('avater/'))),
                ('border_color', models.CharField(blank=True, null=True, max_length=10)),
                ('border_width', models.IntegerField(blank=True, null=True)),
                ('role', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('contact', models.EmailField(blank=True, null=True, max_length=70)),
                ('website', models.URLField(verbose_name='Website', blank=True, null=True)),
                ('linkedin', models.URLField(verbose_name='LinkedIn', blank=True, null=True)),
                ('facebook', models.URLField(verbose_name='Facebook', blank=True, null=True)),
                ('twitter', models.URLField(verbose_name='Twitter', blank=True, null=True)),
                ('googleplus', models.URLField(verbose_name='Google+', blank=True, null=True)),
                ('github', models.URLField(verbose_name='Github', blank=True, null=True)),
                ('hackernews', models.URLField(verbose_name='HackerNews', blank=True, null=True)),
                ('email', models.EmailField(unique=True, max_length=70)),
                ('testimonial', models.TextField()),
                ('testimonial_name', models.CharField(max_length=255)),
                ('testimonial_desig', models.CharField(max_length=70)),
                ('testimonial_link', models.URLField(verbose_name='LinkedIn', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('company', models.CharField(max_length=255)),
                ('website', models.URLField()),
                ('designation', models.CharField(max_length=30)),
                ('content', django_markdown.models.MarkdownField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
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
