# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_work_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='designation',
            field=models.CharField(max_length=100),
        ),
    ]
