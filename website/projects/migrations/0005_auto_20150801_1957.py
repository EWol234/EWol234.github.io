# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_picture_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ForeignKey(to='projects.Picture', default=2),
            preserve_default=False,
        ),
    ]
