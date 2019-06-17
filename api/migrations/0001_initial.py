# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-13 13:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditorium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('no_of_sheets', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Auditorium',
                'verbose_name_plural': 'Auditoriums',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(blank=True, max_length=200, null=True)),
                ('duration', models.CharField(blank=True, max_length=200, null=True)),
                ('cast', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('movie', models.CharField(blank=True, max_length=200, null=True)),
                ('screen_start', models.DateTimeField(auto_now_add=True)),
                ('auditorium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screens', to='api.Auditorium')),
            ],
            options={
                'verbose_name': 'Screen',
                'verbose_name_plural': 'Screens',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('row', models.CharField(max_length=5)),
                ('number', models.CharField(max_length=5)),
                ('auditorium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sheets', to='api.Auditorium')),
            ],
            options={
                'verbose_name': 'Seat',
                'verbose_name_plural': 'Seats',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='screen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screen_bookings', to='api.Screen'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_bookings', to=settings.AUTH_USER_MODEL),
        ),
    ]