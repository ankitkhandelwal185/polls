# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180925_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
