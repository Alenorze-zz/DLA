# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='leave_capture',
            field=models.BooleanField(default=True),
        ),
    ]