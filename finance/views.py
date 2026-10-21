from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .models import Income,Expense
from django.db.models import Sum

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


@login_required
def income_update_view(request, pk):
    income = get_object_or_404(Income, id=pk, user=request.user)

    if request.method == 'POST':
        income.amount = request.POST.get('amount')
        income.category = request.POST.get('category')
        income.description = request.POST.get('description')

        income.save()

        return redirect('income_list')

    return render(request, 'income_update.html', {'income': income })


@login_required
def income_delete_view(request, pk):
    income = get_object_or_404(Income, id=pk, user=request.user)

    if request.method == 'POST':
        income.delete()
        return redirect('income_list')

    return render(request, 'income_delete.html', {'income': income})


@login_required
def expense_list_view(request):
    expenses = Expense.objects.filter(user=request.user)

    return render(request, 'expense_list.html', {'expenses': expenses })


@login_required
def expense_create_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description')

        Expense.objects.create(
            user=request.user,
            amount=amount,
            category=category,
            description=description
        )

        return redirect('expense_list')
    return render(request, 'expense_create.html')


@login_required
def expense_update_view(request, pk):
    expense = get_object_or_404(Expense, id=pk, user=request.user)

    if request.method == 'POST':
        expense.amount = request.POST.get('amount')
        expense.category = request.POST.get('category')
        expense.description = request.POST.get('description')

        expense.save()

        return redirect('expense_list')
    return render(request, 'expense_update.html', {'expense': expense})


@login_required
def expense_delete_view(request, pk):
    expense = get_object_or_404(Expense, id=pk, user=request.user)

    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')

    return render(request, 'expense_delete.html', {
        'expense': expense
    })




@login_required
def summary_income_view(request):
    total_income = Income.objects.filter(user=request.user
    ).aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'summary_income.html', {'total_income': total_income})


@login_required
def summary_expense_view(request):
    total_expense = Expense.objects.filter(user=request.user
    ).aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'summary_expense.html', {'total_expense': total_expense})


@login_required
def summary_view(request):
    total_income = Income.objects.filter(
        user=request.user
    ).aggregate(total=Sum('amount'))['total'] or 0

    total_expense = Expense.objects.filter(
        user=request.user
    ).aggregate(total=Sum('amount'))['total'] or 0

    balance = total_income - total_expense
    return render(request, 'summary.html', {'total_income': total_income, 'total_expense': total_expense, 'balance': balance})




