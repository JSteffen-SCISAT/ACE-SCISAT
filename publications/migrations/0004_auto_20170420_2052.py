# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20170420_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='publications/publications/', verbose_name='PDF'),
        ),
    ]
