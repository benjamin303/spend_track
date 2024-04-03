import calendar
import datetime
from django.shortcuts import render
from expense.models import Expense, MethodOfPayment
from income.models import Income, MethodOfIncome
from django.db.models import Sum, IntegerField
from itertools import chain
from .forms import DateFilterForm
from django.db.models.functions import Cast, ExtractMonth

# Create your views here.
def index(request):
    
    #last expenses and incomes
    last_three_expenses = Expense.objects.order_by('-date')[:3]
    last_three_income = Income.objects.order_by('-date')[:3]
    
    #calculate total expenses and incomes
    total_expense = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_income = Income.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    #balance
    balance = total_income - total_expense
    
    # query set of month, and total expense by month
    expenses_by_month_qs = Expense.objects.annotate(
        month=Cast(ExtractMonth('date'), IntegerField())
    ).values('month').annotate(total=Sum('amount')).order_by('month')

    # query set of month, and total incomes by month
    incomes_by_month_qs = Income.objects.annotate(
        month=Cast(ExtractMonth('date'), IntegerField())
    ).values('month').annotate(total=Sum('amount')).order_by('month')
    
    # list of monthly expenses
    expenses_by_month = {
        'total_expenses_by_months':  list(expenses_by_month_qs.values_list('total', flat=True)),
    }

    # list of monthly incomes
    incomes_by_month = {
        'total_incomes_by_months': list(incomes_by_month_qs.values_list('total', flat=True)),
    }

    # all months 
    months_expenses = [calendar.month_abbr[month['month']] for month in expenses_by_month_qs]
    months_incomes = [calendar.month_abbr[month['month']] for month in incomes_by_month_qs]
    all_months = sorted(set(months_expenses + months_incomes), key=lambda x: datetime.datetime.strptime(x, "%b"))

    context = {
        'last_three_expenses': last_three_expenses,
        'last_three_incomes': last_three_income,
        'total_expense': total_expense,
        'total_income': total_income,
        'balance': balance,
        'expenses_by_month': expenses_by_month,
        'incomes_by_month': incomes_by_month,
        'months': all_months,
    }
    
    return render(request, 'balance/index.html', context)

def transactions(request):
    AllIncomes = Income.objects.order_by('-date').all()
    AllExpenses = Expense.objects.order_by('-date').all()
    
    combined_list = list(chain(AllIncomes, AllExpenses))
    
    combined_sorted = sorted(combined_list, key=lambda instance:instance.date, reverse=True)
    context = {
        'combined_transactions': combined_sorted
    }
    return render(request, 'transactions/index.html', context)
