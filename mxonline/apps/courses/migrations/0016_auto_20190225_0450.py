# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-25 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_lesson_chapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='chapter',
        ),
        migrations.AddField(
            model_name='lesson',
            name='type',
            field=models.CharField(choices=[('xj', '\u5c0f\u8282'), ('dj', '\u5927\u8282')], default='xj', max_length=2),
        ),
    ]