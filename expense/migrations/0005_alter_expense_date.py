# Generated by Django 3.2.12 on 2024-01-29 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_expense_methodofpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]