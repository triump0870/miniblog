# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170103_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='resume',
            field=models.FileField(blank=True, upload_to=blog.models.generatefilename('resume/'), null=True),
        ),
    ]
