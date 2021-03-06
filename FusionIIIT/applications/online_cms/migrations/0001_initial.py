# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-08 14:40
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic_information', '0001_initial'),
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(auto_now=True)),
                ('submit_date', models.DateTimeField()),
                ('assignment_name', models.CharField(max_length=100)),
                ('assignment_url', models.CharField(max_length=100, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=100)),
                ('document_name', models.CharField(max_length=40)),
                ('document_url', models.CharField(max_length=100, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=100)),
                ('video_name', models.CharField(max_length=40)),
                ('video_url', models.CharField(max_length=100, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_time', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(max_length=2000)),
                ('commenter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Course')),
            ],
        ),
        migrations.CreateModel(
            name='ForumReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_ques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_ques', to='online_cms.Forum')),
                ('forum_reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_reply', to='online_cms.Forum')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=20)),
                ('end_time', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('d_day', models.CharField(max_length=2)),
                ('d_hour', models.CharField(max_length=2)),
                ('d_minute', models.CharField(max_length=2)),
                ('negative_marks', models.FloatField(default=0)),
                ('number_of_question', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=1000)),
                ('rules', models.TextField(max_length=2000)),
                ('total_score', models.IntegerField(default=0)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Course')),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000)),
                ('options1', models.CharField(max_length=100, null=True)),
                ('options2', models.CharField(max_length=100, null=True)),
                ('options3', models.CharField(max_length=100, null=True)),
                ('options4', models.CharField(max_length=100, null=True)),
                ('options5', models.CharField(max_length=100, null=True)),
                ('answer', models.IntegerField()),
                ('announcement', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.TextField(max_length=1000, null=True)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_cms.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('finished', models.BooleanField(default=False)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_cms.Quiz')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.IntegerField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_cms.QuizQuestion')),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_cms.Quiz')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(auto_now=True)),
                ('upload_url', models.TextField(max_length=200)),
                ('score', models.IntegerField(null=True)),
                ('feedback', models.CharField(max_length=100, null=True)),
                ('assign_name', models.CharField(max_length=100)),
                ('assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_cms.Assignment')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
        ),
    ]
