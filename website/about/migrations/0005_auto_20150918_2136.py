# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20150918_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='parent',
            field=models.ForeignKey(to='about.Category', blank=True, null=True),
        ),
    ]
