# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 18:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0002_auto_20170223_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
    ]
