from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
import datetime
def home(request):
    return render(request,'crud/home.html')

def register_form(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'crud/register.html', {'form': form})

def login_form(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'crud/login.html', {'form': form})

def logout_form(request):
  logout(request)
  return redirect('login')

def action(request):
  return render(request,'crud/action.html')

def sports(request):
    return render(request,'crud/sports.html')
def strategy(request):
    return render(request,'crud/strategy.html')
