# Generated by Django 2.2 on 2020-10-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parksystemapp', '0004_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(blank=True, choices=[('Credit Card', 'Credit Card'), ('Android Pay', 'Android Pay'), ('PayPal', 'PayPal'), ('ApplePay', 'ApplePay')], default='', max_length=255, null=True),
        ),
    ]