from django.db import models
from category.models import ExpenseCategory
from category.models import ExpenseSubCategory
from django.utils.translation import gettext as _
import datetime

# Create your models here.

class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(ExpenseSubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    methodofpayment = models.ForeignKey('MethodOfPayment', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(_("Date"), default=datetime.date.today)
    description = models.TextField(null=True, blank=True)
    
    # Not working because ordering is already set in views.py: ".order_by('date', 'amount')"
    # class Meta:
    #     ordering = ['-date', '-amount']
    
    def __str__(self):
        return f"{self.amount}  - {self.category.name} - {self.subcategory.name if self.subcategory else 'No Subcategory'}"
    
    def get_transaction_type(self):
        return "Expense"

class MethodOfPayment(models.Model):
    method = models.CharField(max_length=100)

    def __str__(self):
        return self.method