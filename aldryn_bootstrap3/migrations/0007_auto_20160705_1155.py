# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 15:55
from __future__ import unicode_literals

from django.db import migrations
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_bootstrap3', '0006_auto_20160615_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boostrap3buttonplugin',
            name='link_attributes',
            field=djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Link Attributes'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='link_attributes',
            field=djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Link Attributes'),
        ),
    ]