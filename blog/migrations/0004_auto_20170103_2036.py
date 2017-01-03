# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_userdata_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.generatefilename('avatar/')),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='resume',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.generatefilename('resume/')),
        ),
    ]
