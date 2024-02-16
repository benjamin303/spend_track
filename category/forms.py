from django.forms import ModelForm
from .models import IncomeCategory, ExpenseCategory, ExpenseSubCategory

class IncomeCategoryForm(ModelForm):
    class Meta:
        model = IncomeCategory
        fields = '__all__'

class ExpenseCategoryForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'
        
class ExpenseSubCategoryForm(ModelForm):
    class Meta:
        model = ExpenseSubCategory
        fields = '__all__'