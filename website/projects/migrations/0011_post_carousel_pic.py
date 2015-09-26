# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20150918_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='carousel_pic',
            field=models.ForeignKey(null=True, to='projects.Picture', blank=True, related_name='carousel'),
        ),
    ]
