from django.http import HttpResponse
from django.template import loader
from .models import Expense
from django.shortcuts import render, redirect
from .forms import ExpenseForm

# Create your views here.

def index(request):
    myexpenses = Expense.objects.order_by('date', 'amount').select_related('category', 'subcategory', 'methodofpayment').all()
    context = {
        'myexpenses': myexpenses,
    }
    return render(request, 'index.html', context)

def addExpense(request):
    form = ExpenseForm()
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            print('Form is successfully. It work!')
            return redirect('list')
        else:
            print('Error')
            print('Form errors:', form.errors)
        
    context = {'form': form}
    return render(request, 'addExpense.html', context)

def list(request):
    myexpenses = Expense.objects.order_by('-date', 'amount').select_related('category', 'subcategory', 'methodofpayment').all()
    context = {
        'myexpenses': myexpenses,
    }
    return render(request, 'list.html', context)

def edit(request, id):
    expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=expense)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('/list')
    
    context = {'form': form}
    return render(request, 'edit.html', context)
    
def details(request, id):
    myexpense = Expense.objects.get(id=id)
    context = {
        'myexpense': myexpense,
    }
    return render(request, 'details.html', context)
    
def delete(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('list')
    return render(request, 'delete.html', {'obj':expense})

