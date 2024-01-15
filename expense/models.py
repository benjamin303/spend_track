from django.db import models
from category.models import Category
from category.models import SubCategory

# Create your models here.

class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    methodofpayment = models.ForeignKey('MethodOfPayment', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.amount}  - {self.category.name} - {self.subcategory.name if self.subcategory else 'No Subcategory'}"

class MethodOfPayment(models.Model):
    method = models.CharField(max_length=100)

    def __str__(self):
        return self.method
    