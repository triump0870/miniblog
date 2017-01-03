# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170103_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='image',
            new_name='avatar',
        ),
    ]
