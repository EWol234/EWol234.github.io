# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150730_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('address', models.CharField(max_length=1000)),
                ('order', models.IntegerField()),
                ('post', models.ForeignKey(to='projects.Post')),
            ],
        ),
    ]
