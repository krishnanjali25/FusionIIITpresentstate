# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-08 11:11
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
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_bill', models.IntegerField(default=0)),
                ('room_bill', models.IntegerField(default=0)),
                ('payment_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BookingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_category', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('person_count', models.IntegerField(default=1)),
                ('purpose', models.TextField(blank=True)),
                ('booking_from', models.DateField()),
                ('booking_to', models.DateField()),
                ('check_in', models.DateField(blank=True, null=True)),
                ('check_out', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Canceled', 'Canceled'), ('CheckedIn', 'CheckedIn'), ('Complete', 'Complete')], default='Pending', max_length=10)),
                ('remark', models.CharField(blank=True, max_length=40, null=True)),
                ('intender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=0)),
                ('consumable', models.BooleanField(default=False)),
                ('opening_stock', models.IntegerField(default=0)),
                ('addition_stock', models.IntegerField(default=0)),
                ('total_stock', models.IntegerField(default=0)),
                ('serviceable', models.IntegerField(default=0)),
                ('non_serviceable', models.IntegerField(default=0)),
                ('inuse', models.IntegerField(default=0)),
                ('total_usable', models.IntegerField(default=0)),
                ('remark', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(max_length=40)),
                ('cost', models.IntegerField(default=0)),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_hostel.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='MealRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_date', models.DateField()),
                ('morning_tea', models.BooleanField(default=False)),
                ('eve_tea', models.BooleanField(default=False)),
                ('breakfast', models.BooleanField(default=False)),
                ('lunch', models.BooleanField(default=False)),
                ('dinner', models.BooleanField(default=False)),
                ('persons', models.IntegerField(default=0)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_hostel.BookingDetail')),
            ],
        ),
        migrations.CreateModel(
            name='RoomDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=4, unique=True)),
                ('room_type', models.CharField(choices=[('SingleBed', 'SingleBed'), ('DoubleBed', 'DoubleBed'), ('VIP', 'VIP')], max_length=12)),
                ('room_floor', models.CharField(choices=[('GroundFloor', 'GroundFloor'), ('FirstFloor', 'FirstFloor'), ('SecondFloor', 'SecondFloor'), ('ThirdFloor', 'ThirdFloor')], max_length=12)),
                ('room_status', models.CharField(choices=[('Booked', 'Booked'), ('CheckedIn', 'CheckedIn'), ('Available', 'Available'), ('UnderMaintenance', 'UnderMaintenance')], default='Available', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_phone', models.CharField(max_length=15, unique=True)),
                ('visitor_name', models.CharField(max_length=40)),
                ('visitor_email', models.CharField(blank=True, max_length=40)),
                ('visitor_organization', models.CharField(blank=True, max_length=100)),
                ('visitor_address', models.TextField(blank=True)),
                ('nationality', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='mealrecord',
            name='visitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_hostel.VisitorDetail'),
        ),
        migrations.AddField(
            model_name='bookingdetail',
            name='rooms',
            field=models.ManyToManyField(to='visitor_hostel.RoomDetail'),
        ),
        migrations.AddField(
            model_name='bookingdetail',
            name='visitor',
            field=models.ManyToManyField(to='visitor_hostel.VisitorDetail'),
        ),
        migrations.AddField(
            model_name='bill',
            name='booking',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='visitor_hostel.BookingDetail'),
        ),
        migrations.AddField(
            model_name='bill',
            name='caretaker',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
