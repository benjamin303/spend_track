from django.shortcuts import render, redirect
from .models import Income
from .forms import IncomeForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    incomes = Income.objects.order_by('-date', 'amount').select_related('category', 'methodofincome').all()
    context = {
        'incomes': incomes,
    }
    return render(request, 'income/index.html', context)

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