# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170226_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
