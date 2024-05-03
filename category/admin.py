from django.contrib import admin
from .models import ExpenseCategory, ExpenseSubCategory, IncomeCategory, ExpenseCompanies

# Register your models here.

admin.site.register(ExpenseCategory)
admin.site.register(ExpenseSubCategory)
admin.site.register(IncomeCategory)
admin.site.register(ExpenseCompanies)