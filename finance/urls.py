from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('income/', views.income_list_view, name='income_list'),
    path('income/create/', views.income_create_view, name='income_create'),
    path('income/<int:pk>/update/', views.income_update_view, name='income_update'),
    path('income/<int:pk>/delete/', views.income_delete_view, name='income_delete'),

    path('expense/', views.expense_list_view, name='expense_list'),
    path('expense/create/', views.expense_create_view, name='expense_create'),
    path('expense/<int:pk>/update/', views.expense_update_view, name='expense_update'),
    path('expense/<int:pk>/delete/', views.expense_delete_view, name='expense_delete'),

    path('summary/income/', views.summary_income_view, name='summary_income'),
    path('summary/expense/', views.summary_expense_view, name='summary_expense'),
    path('summary/', views.summary_view, name='summary'),
]
