# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+919999999990'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], max_length=10),
        ),
    ]
