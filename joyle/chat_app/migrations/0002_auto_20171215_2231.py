# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 22:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2017, 12, 15, 22, 31, 24, 505815, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 12, 15, 22, 31, 24, 506558, tzinfo=utc)),
        ),
    ]
