# Generated by Django 2.2 on 2020-10-06 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parksystemapp', '0002_auto_20201006_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('property_report_time', models.DateTimeField()),
                ('property_status_description', models.TextField(default='')),
                ('property_expenses', models.IntegerField(blank=True, null=True)),
                ('property_status_notes', models.TextField(default='')),
                ('maint_staff_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('property_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status.propertyname+', to='parksystemapp.ParkProperty')),
                ('reservation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status.resid+', to='parksystemapp.Reservation')),
            ],
        ),
    ]