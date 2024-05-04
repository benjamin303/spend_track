from .models import Expense
from django.shortcuts import render, redirect
from .forms import ExpenseForm
from django.db.models import Min, Max
from .models import Expense
import calendar
import datetime

# Create your views here.

def index(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    current_date = datetime.date.today()
    month = int(month) if month and month.isdigit() else None
    year = int(year) if year and year.isdigit() else current_date.year

    # Finding min and max year from the database.
    year_range = Expense.objects.aggregate(min_year=Min('date__year'), max_year=Max('date__year'))
    years = range(year_range['min_year'], year_range['max_year'] + 1)
    months = [(i, calendar.month_name[i]) for i in range(1, 13)]

    if month:
        myexpenses = Expense.objects.filter(date__year=year, date__month=month)
    else:
        myexpenses = Expense.objects.filter(date__year=year)

    myexpenses = myexpenses.order_by('date', 'amount').select_related('category', 'subcategory', 'methodofpayment')

    context = {
        'myexpenses': myexpenses,
        'months': months,
        'month_selected': month,
        'years': years,
        'year_selected': year,
    }
    return render(request, 'expense/index.html', context)


def add(request):
    form = ExpenseForm()
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            print('Form is successfully. It work!')
            return redirect('/expense')
        else:
            print('Error')
            print('Form errors:', form.errors)
        
    context = {'form': form}
    return render(request, 'expense/add.html', context)

def edit(request, id):
    expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=expense)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('/expense')
    
    context = {'form': form}
    return render(request, 'expense/edit.html', context)
    
def details(request, id):
    myexpense = Expense.objects.get(id=id)
    context = {
        'myexpense': myexpense,
    }
    return render(request, 'expense/details.html', context)
    
def delete(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('/expense')
    return render(request, 'expense/delete.html', {'obj':expense})

