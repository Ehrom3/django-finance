from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .models import Income,Expense

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not username and not password:
            return render(request, "register.html",{"error":"Username is required"})
        
        if password != password2:
            return render(request, "register.html ", {"error": "Password do not match"})
        
        if User.objects.filter(username=username).exists():
            return render(request, "register.html" ,{"error":"Username already exists"})
        
        User.objects.create_user(username=username,password=password)
        return redirect("login")
    return render(request, "register.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username , password=password)

        if user is None:
            return render(request, 'login.html', {'error':'Mistake login or password'})
        
        login(request, user)
        return redirect('home')
    
    return render(request, 'login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('home')

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def income_list_view(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'income_list.html', {'incomes':incomes})

@login_required
def income_create_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description')

        Income.objects.create(user=request.user, amount=amount, category=category, description=description)
        return redirect('income_list')
    return render(request, 'income_create.html')






