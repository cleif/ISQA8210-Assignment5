# Generated by Django 2.2.13 on 2020-12-12 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parksystemapp', '0006_remove_propertystatus_property_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkproperty',
            name='property_slot',
        ),
    ]
