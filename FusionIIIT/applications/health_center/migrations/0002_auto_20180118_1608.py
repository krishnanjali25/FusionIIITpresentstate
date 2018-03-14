# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 16:08
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='doctor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.Doctor'),
        ),
    ]
