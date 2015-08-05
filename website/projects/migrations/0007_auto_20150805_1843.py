# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20150805_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='matching_post',
            field=models.ForeignKey(to='projects.Post', blank=True, null=True),
        ),
    ]
