# Generated by Django 3.2.12 on 2024-02-10 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0007_alter_expense_category'),
        ('category', '0004_rename_expense_category_expensecategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expense_SubCategory',
            new_name='ExpenseSubCategory',
        ),
    ]
