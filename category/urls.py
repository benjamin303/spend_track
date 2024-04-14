from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addIncomeCategory', views.addIncomeCategory, name='addIncomeCategory'),
    path('addExpenseCategory', views.addExpenseCategory, name='addExpenseCategory'),
    path('subcategories/', views.subcategories, name='category_subcategories'),
]
