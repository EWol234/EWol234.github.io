# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20150918_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
    ]
