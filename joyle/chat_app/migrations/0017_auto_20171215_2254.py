# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 22:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0016_auto_20171215_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2017, 12, 15, 22, 54, 22, 34005, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 12, 15, 22, 54, 22, 34694, tzinfo=utc)),
        ),
    ]
