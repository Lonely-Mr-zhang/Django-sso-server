# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas', '0007_auto_20180925_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='agentid',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='options',
            name='appid',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='options',
            name='redirect_uri',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='options',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
