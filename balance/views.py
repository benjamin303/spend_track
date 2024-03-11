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

    balance = total_income - total_expense
    
    
    
    # form = DateFilterForm(request.GET)
    
    # filtered_incomes = Income.objects.all()
    # filtered_expenses = Expense.objects.all()
    
    # if form.is_valid():
    #     year = form.cleaned_data.get('year')
    #     month = form.cleaned_data.get('month')
    #     day = form.cleaned_data.get('day')
        
    #     if year:
    #         filtered_expenses = filtered_expenses.filter(date__year=year)
    #         filtered_incomes = filtered_incomes.filter(date__year=year)
    #     if month:
    #         filtered_expenses = filtered_expenses.filter(date__month=month)
    #         filtered_incomes = filtered_incomes.filter(date__month=month)
    #     if day:
    #         filtered_expenses = filtered_expenses.filter(date__day=day)
    #         filtered_incomes = filtered_incomes.filter(date__day=day)

    # raw_incomes_sum = filtered_incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    # raw_expenses_sum = filtered_expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    
    # total_incomes = round(raw_incomes_sum)
    # total_expenses = round(raw_expenses_sum)


    expenses_by_month_qs = Expense.objects.annotate(
        month=Cast(ExtractMonth('date'), IntegerField())
    ).values('month').annotate(total=Sum('amount')).order_by('month')

    # months = list(expenses_by_month_qs.values_list('month', flat=True))
    totals = list(expenses_by_month_qs.values_list('total', flat=True))

    expenses_by_month = {
        # 'months': months,
        'totals': totals,
    }

    incomes_by_month_qs = Income.objects.annotate(
        month=Cast(ExtractMonth('date'), IntegerField())
    ).values('month').annotate(total=Sum('amount')).order_by('month')

    # months = list(incomes_by_month_qs.values_list('month', flat=True))
    totals = list(incomes_by_month_qs.values_list('total', flat=True))

    incomes_by_month = {
        # 'months': months,
        'totals': totals,
    }
        
    context = {
        'last_three_expenses': last_three_expenses,
        'last_three_incomes': last_three_income,
        'total_expense': total_expense,
        'total_income': total_income,
        'balance': balance,
        # 'form': form,
        # 'expenses': filtered_expenses,
        # 'incomes': filtered_incomes,
        # 'total_expenses': total_expenses,
        # 'total_incomes': total_incomes,
        'expenses_by_month': expenses_by_month,
        'incomes_by_month': incomes_by_month,
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
