# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-09 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address1', models.CharField(max_length=256)),
                ('address2', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('song_request', models.CharField(blank=True, max_length=256, null=True)),
                ('guests', models.IntegerField()),
                ('attending', models.BooleanField()),
            ],
        ),
    ]
