# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150801_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='picture',
            new_name='thumbnail',
        ),
        migrations.AddField(
            model_name='picture',
            name='matching_post',
            field=models.ForeignKey(default=1, to='projects.Post'),
            preserve_default=False,
        ),
    ]
