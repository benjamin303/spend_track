from django import forms
from django.forms import ModelForm
from .models import Income

class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ["category", "methodofincome", "amount", "description"]
        widgets = {
            "category": forms.Select(attrs={"class": "form-select"}),
            "subcategory": forms.Select(attrs={"class": "form-select"}),
            "methodofincome": forms.Select(attrs={"class": "form-select"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the default value for methodofincome
        self.fields["methodofincome"].initial = 1  # default value is card
