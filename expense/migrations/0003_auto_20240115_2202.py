# Generated by Django 3.2.12 on 2024-01-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_expense_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MethodOfPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
