from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name= "login"), 
    path('logout/', views.logout_view, name='logout'),
    path('income/', views.income_list_view, name='income_list'),
    path('income/create/', views.income_create_view, name='income_create')

    
]
