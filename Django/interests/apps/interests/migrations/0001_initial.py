# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'interests',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=200)),
                ('last_name', models.TextField(max_length=200)),
                ('age', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('occupation', models.TextField(max_length=200)),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interests.Interest')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
