# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-02 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0018_auto_20180401_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Event_ID',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='Org_ID',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
