# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170101_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='resume',
            field=models.FileField(null=True, upload_to=blog.models.generatefilename('resume/'), blank=True),
        ),
    ]
