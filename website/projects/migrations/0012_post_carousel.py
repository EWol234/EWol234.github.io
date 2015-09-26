# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_post_carousel_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='carousel',
            field=models.NullBooleanField(),
        ),
    ]
