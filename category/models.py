from django.db import models

# Create your models here.
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class ExpenseSubCategory(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class IncomeCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class ExpenseCompanies(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(ExpenseCategory)
    # parent_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)

    def __str__(self):
        # return self.name
        return f"{self.name}  - {self.categories}"
