from django.contrib import admin
from .models import ExpenseCategory, ExpenseSubCategory, IncomeCategory

# Register your models here.

admin.site.register(ExpenseCategory)
admin.site.register(ExpenseSubCategory)
admin.site.register(IncomeCategory)
