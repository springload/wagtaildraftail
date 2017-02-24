# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 10:15
from __future__ import absolute_import, unicode_literals

import wagtail.wagtailcore.fields
from django.db import migrations

import wagtaildraftail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body_draftail',
            field=wagtaildraftail.fields.DraftailTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_hallo',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
