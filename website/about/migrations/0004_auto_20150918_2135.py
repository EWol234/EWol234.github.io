# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_category_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('order', models.IntegerField()),
                ('parent', models.ForeignKey(to='about.Subcategory', blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
