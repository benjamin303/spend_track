from django.contrib import admin
from .models import Expense, MethodOfPayment


# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("amount", "methodofpayment", "category", "subcategory", "date")
admin.site.register(Expense, ExpenseAdmin)

admin.site.register(MethodOfPayment)

