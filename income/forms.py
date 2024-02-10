from django.forms import ModelForm
from .models import Income

class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = '__all__'