# Generated by Django 3.2.12 on 2024-02-11 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0003_transaction_current_balance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
