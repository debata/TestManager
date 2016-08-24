# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 00:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_auto_20160817_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(editable=False)),
                ('comment_body', models.TextField()),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('defect', models.ManyToManyField(blank=True, null=True, to='main.TestCase')),
                ('test_result', models.ManyToManyField(blank=True, null=True, to='main.TestResult')),
                ('test_session', models.ManyToManyField(blank=True, null=True, to='main.TestSession')),
            ],
        ),
    ]
