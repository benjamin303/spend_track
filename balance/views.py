from django.shortcuts import render
from expense.models import Expense, MethodOfPayment
from income.models import Income, MethodOfIncome
from django.db.models import Sum

# Create your views here.
def index(request):
    
    #last expenses and incomes
    last_three_expenses = Expense.objects.order_by('-date')[:3]
    last_three_income = Income.objects.order_by('-date')[:3]
    
    #calculate total expenses and incomes
    total_expense = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_incomes = Income.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    card_payment_method = MethodOfPayment.objects.filter(method='card').first()
    if card_payment_method:
        total_expense_card = Expense.objects.filter(methodofpayment=card_payment_method).aggregate(Sum('amount'))['amount__sum'] or 0
    else:
        total_expense_card = 0
    cash_payment_method = MethodOfPayment.objects.filter(method='cash').first()
    if cash_payment_method:
        total_expense_cash = Expense.objects.filter(methodofpayment=cash_payment_method).aggregate(Sum('amount'))['amount__sum'] or 0
    else:
        total_expense_cash = 0
        
    card_income_method = MethodOfIncome.objects.filter(method='card').first()
    if card_income_method:
        total_income_card = Income.objects.filter(methodofincome=card_income_method).aggregate(Sum('amount'))['amount__sum'] or 0
    else:
        total_expense_card = 0
    cash_income_method = MethodOfIncome.objects.filter(method='cash').first()
    if cash_income_method:
        total_income_cash = Income.objects.filter(methodofincome=cash_income_method).aggregate(Sum('amount'))['amount__sum'] or 0
    else:
        total_income_cash = 0
    
    
    #calculate balance
    balance = total_incomes - total_expense
        
    context = {
        'last_three_expenses': last_three_expenses,
        'last_three_incomes': last_three_income,
        'total_expense': total_expense,
        'total_incomes': total_incomes,
        'balance': balance,
        'total_expense_card': total_expense_card,
        'total_expense_cash': total_expense_cash,
        'total_income_card': total_income_card,
        'total_income_cash': total_income_cash,
    }
    
    
    
    return render(request, 'balance/index.html', context)