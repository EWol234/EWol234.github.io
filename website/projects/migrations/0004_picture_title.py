# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='title',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
