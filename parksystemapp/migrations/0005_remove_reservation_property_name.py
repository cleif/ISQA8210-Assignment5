# Generated by Django 2.2.13 on 2020-12-06 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parksystemapp', '0004_auto_20201204_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='property_name',
        ),
    ]