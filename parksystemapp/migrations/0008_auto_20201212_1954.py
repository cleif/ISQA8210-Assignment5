# Generated by Django 2.2.13 on 2020-12-13 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parksystemapp', '0007_remove_parkproperty_property_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertystatus',
            name='property_report_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
