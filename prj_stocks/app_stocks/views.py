from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from app_stocks.models import Stock
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

class Myclass(View):
    def get(self,request):
        return render(request,"home.html")

def loginPage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=uname).exists():
            messages.error(request,"Username doesn't exist")
            return render(request, "login.html")
        
        user=authenticate(request,username=uname,password=password)

        if user is None:
            messages.error(request,"Invalid Password")
            return render(request, "login.html")
        else:
            login(request, user)  # Log the user in
            messages.success(request, "Login Successful!")
            return redirect('show')
        
    return render(request,"login.html")

def registerUser(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username=uname).exists():
            messages.error(request,"Username already exists")
            return render(request, "register.html")
        else:
            User.objects.create_user(username=uname,password=password)
            messages.success(request,"User created successfully")
            return redirect('login')
    
    return render(request,"register.html")
    
class StockCreate(CreateView):
    model=Stock
    template_name="create.html"
    fields='__all__'
    success_url=reverse_lazy("show")
    
class StockList(ListView):
    model=Stock
    template_name="stockdetails.html"


class StockUpdate(UpdateView):
    model=Stock
    fields='__all__'
    template_name="create.html"
    success_url=reverse_lazy("show")

class StockDelete(DeleteView):
    model=Stock
    fields="__all__"
    template_name="delete.html"
    success_url=reverse_lazy("show")
