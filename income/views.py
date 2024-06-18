from django.shortcuts import render, redirect
from .models import Income
from .forms import IncomeForm
from django.db.models import Min, Max
import calendar
import datetime

# Create your views here.

def index(request):
    current_date = datetime.date.today()
    
    month = request.GET.get('month')
    year = request.GET.get('year')
    order = request.GET.get('order', '')
    
    if not month and not year:
        month = None
        year = current_date.year
    else:
        # Convert to integers if provided
        month = int(month) if month and month.isdigit() else None
        year = int(year) if year and year.isdigit() else current_date.year
        
    year_range = Income.objects.aggregate(min_year=Min('date__year'), max_year=Max('date__year'))
    years = range(year_range['min_year'], year_range['max_year'] + 1)
    months = [(i, calendar.month_name[i]) for i in range(1, 13)]
    
    if month:
        incomes = Income.objects.filter(date__year=year, date__month=month)
    else:
        incomes = Income.objects.filter(date__year=year)
        
    if order == 'asc':
        incomes = incomes.order_by('amount', '-date').select_related('category', 'methodofincome')
    elif order == 'desc':
        incomes = incomes.order_by('-amount', '-date').select_related('category', 'methodofincome')
    else:
        incomes = incomes.order_by('-date', 'amount').select_related('category', 'methodofincome')
        

    context = {
        'incomes': incomes,
        'order': order,
        'months': months,
        'month_selected': month,
        'years': years,
        'year_selected': year,
    }
    return render(request, 'income/index.html', context)

def details(request, id):
    income = Income.objects.get(id=id)
    context = {
        'income': income
    }
    return render(request, 'income/details.html', context)

def add(request):
    form = IncomeForm()
    
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            print('Form is successfully. It work!')
            return redirect('/income')
        else:
            print('Form errors: ', form.errors)
    context = {'form': form}
    return render(request, 'income/add.html', context)

def edit(request, id):
    income = Income.objects.get(id=id)
    form = IncomeForm(instance=income)
    
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('/income')

    context = {'form': form}
    return render(request, 'income/edit.html', context)

def delete(request, id):
    income = Income.objects.get(id=id)
    if request.method == 'POST':
        income.delete()
        return redirect('/income')
    return render(request, 'income/delete.html', {'obj':income})