from django.forms import ModelForm
from .models import IncomeCategory, ExpenseCategory, ExpenseSubCategory, ExpenseCompanies

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
        
class ExpenseCompaniesForm(ModelForm):
    class Meta:
        model = ExpenseCompanies
        fields = '__all__'