# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='caption',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ForeignKey(to='projects.Picture', blank=True),
        ),
    ]
