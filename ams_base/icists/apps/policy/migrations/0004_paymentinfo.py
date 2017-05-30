# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-21 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0003_auto_20151218_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('bank_branch', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=100)),
                ('recipient_name', models.CharField(max_length=100)),
                ('swift_code', models.CharField(max_length=100)),
            ],
        ),
    ]
