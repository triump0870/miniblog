# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='stack_overflow',
            field=models.URLField(verbose_name='Stack Overflow', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='resume',
            field=models.FileField(blank=True, upload_to='resume/', null=True),
        ),
    ]
