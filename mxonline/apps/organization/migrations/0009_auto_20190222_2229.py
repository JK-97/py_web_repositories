# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-22 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '\u57f9\u8bad\u673a\u6784'), ('gr', '\u4e2a\u4eba'), ('gx', '\u9ad8\u6821')], default='pxjg', max_length=10, verbose_name='\u673a\u6784\u7c7b\u578b'),
        ),
    ]