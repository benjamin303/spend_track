from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import IncomeCategory, ExpenseCategory, ExpenseSubCategory
from .forms import IncomeCategoryForm, ExpenseCategoryForm, ExpenseSubCategoryForm

# Create your views here.

def index(request):
    income_categories = IncomeCategory.objects.order_by('name').all()
    expense_categories = ExpenseCategory.objects.order_by('name').all()
    expense_subcategories = ExpenseSubCategory.objects.order_by('name').all()
    
    context = {
        'income_categories': income_categories,
        'expense_categories': expense_categories,
        'expense_subcategories': expense_subcategories
    }
    return render(request, 'category/index.html', context)

    # select a subcategory depend on the selected category
def subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = ExpenseSubCategory.objects.filter(parent_category_id=category_id).values('id', 'name')
    return JsonResponse({'subcategories': list(subcategories)})

def addIncomeCategory(request):
    form = IncomeCategoryForm()
    income_categories = IncomeCategory.objects.order_by('name').all()

    
    if request.method == 'POST':
        form = IncomeCategoryForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            print('Income Category added.')
            return redirect('/category')
        else:
            print('Form errors:', form.errors)
        
    context = {
        'form': form,
        'income_categories': income_categories
        }
    return render(request, 'category/addIncomeCategory.html', context)

def addExpenseCategory(request):
    form = ExpenseCategoryForm()
    expense_categories = ExpenseCategory.objects.order_by('name').all()
    
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            print('Expense Category added.')
            return redirect('/category')
        else:
            print('Form errors:', form.errors)
        
    context = {
        'form': form,
        'expense_categories': expense_categories
        }
    return render(request, 'category/addExpenseCategory.html', context)