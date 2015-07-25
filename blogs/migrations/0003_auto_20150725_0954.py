# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20150720_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 7, 53, 52, 134906, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 7, 54, 1, 534668, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
