from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["category", "subcategory", "methodofpayment", "amount", "description"]
        widgets = {
            "category": forms.Select(attrs={"class": "form-select"}),
            "subcategory": forms.Select(attrs={"class": "form-select"}),
            "methodofpayment": forms.Select(attrs={"class": "form-select"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the default value for methodofpayment
        self.fields["methodofpayment"].initial = 1  # default value is card
