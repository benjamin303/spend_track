from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addExpense', views.addExpense, name='addExpense'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('details/<int:id>', views.details, name='details'),
    path('delete/<int:id>', views.delete, name='delete'),
]

