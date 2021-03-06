# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-15 09:06
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visitor_hostel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(choices=[('Intender', 'Intender'), ('VhCaretaker', 'VhCaretaker'), ('VhIncharge', 'VhIncharge')], default='Intender', max_length=20)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='bookingdetail',
            name='purpose',
            field=models.TextField(default='Hi!'),
        ),
    ]
