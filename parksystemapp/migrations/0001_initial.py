# Generated by Django 2.2 on 2020-10-06 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('park_name', models.CharField(default='', max_length=255)),
                ('park_addr', models.CharField(default='', max_length=255)),
                ('park_image', models.TextField(default='')),
                ('park_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParkProperty',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('property_name', models.CharField(default='', max_length=255)),
                ('property_description', models.TextField(default='')),
                ('property_guest_capacity', models.IntegerField(blank=True, null=True)),
                ('property_location', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('property_price', models.IntegerField(blank=True, null=True)),
                ('property_image', models.TextField(default='')),
                ('property_slot', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('park_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parkname', to='parksystemapp.Park')),
            ],
        ),
    ]
