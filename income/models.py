from django.db import models

# Create your models here.
from category.models import IncomeCategory

class Income(models.Model):
    category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, null=True, blank=True)
    methodofincome = models.ForeignKey('methodofincome', verbose_name=("Method of income"), on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.amount} - {self.category.name} - {self.date}"
    
class MethodOfIncome(models.Model):
    method = models.CharField(max_length=50)
    
    def __str__(self):
        return self.method