# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-13 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181013_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='booked_sheets', to='api.Seat'),
            preserve_default=False,
        ),
    ]
