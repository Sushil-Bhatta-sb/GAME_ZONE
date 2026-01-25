from django.shortcuts import render
from .models import newtaskform
import datetime
def home(request,name):
    return render(request,'crud/home.html',{"name":name.capitalize()})

def index(request):
  now = datetime.datetime.now()
  return render(request, "crud/index.html", {
  "newyear": now.month == 1 and now.day == 1
})
  
def add(request):
  if request.method=='POST':
    form = newtaskform(request.POST)
    if form.is_valid():
      task = form.cleaned_data['task']
      return render(request,'crud/add.html',{'form':form,'task':task})
  else:
    form = newtaskform()
  return render(request,'crud/add.html',{'form':form})