# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='check',
            name='age',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='checksub',
            name='check_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.Check'),
        ),
    ]
