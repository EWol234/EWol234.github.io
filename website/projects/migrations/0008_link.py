# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20150805_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('address', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=100)),
                ('matching_post', models.ForeignKey(to='projects.Post', null=True, blank=True)),
            ],
        ),
    ]
