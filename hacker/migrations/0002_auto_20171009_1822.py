# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='aurthor',
            new_name='author',
        ),
    ]
