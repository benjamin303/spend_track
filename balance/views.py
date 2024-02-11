from django.shortcuts import render
from expense.models import Expense
from income.models import Income
from django.db.models import Sum

# Create your views here.
def index(request):
    
    #last expenses and incomes
    last_three_expenses = Expense.objects.order_by('-date')[:3]
    last_three_income = Income.objects.order_by('-date')[:3]
    
    #calculate total expenses and incomes
    total_expense = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_incomes = Income.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    
    #calculate balance
    balance = total_incomes - total_expense
        
    context = {
        'last_three_expenses': last_three_expenses,
        'last_three_incomes': last_three_income,
        'total_expense': total_expense,
        'total_incomes': total_incomes,
        'balance': balance,
    }
    
    
    
    return render(request, 'index.html', context)