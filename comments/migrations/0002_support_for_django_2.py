# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-02 19:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comment_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
    ]
