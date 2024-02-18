from .models import Expense
from django.shortcuts import render, redirect
from .forms import ExpenseForm

# Create your views here.

def index(request):
    myexpenses = Expense.objects.order_by('-date', 'amount').select_related('category', 'subcategory', 'methodofpayment').all()
    context = {
        'myexpenses': myexpenses,
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

