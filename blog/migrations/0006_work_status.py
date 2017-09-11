# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_work_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='status',
            field=models.CharField(default='p', choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1),
        ),
    ]
