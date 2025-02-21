from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from app_stocks.models import Stock
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.

#Home URL
class Myclass(View):
    def get(self,request):
        return render(request,"home.html")

#Login URL
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

#Register URL
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
    
#CRUD-Create a new Stock
class StockCreate(CreateView):
    model=Stock
    template_name="create.html"
    fields='__all__'
    success_url=reverse_lazy("show")
    
#CRUD-View details of all Stocks
class StockList(ListView):
    model=Stock
    template_name="stockdetails.html"

#CRUD-Udpate a particular stock based on primary key(Stock ID)
class StockUpdate(UpdateView):
    model=Stock
    fields='__all__'
    template_name="create.html"
    success_url=reverse_lazy("show")

#CRUD-Delete a particular stock based on primary key(Stock ID)
class StockDelete(DeleteView):
    model=Stock
    fields="__all__"
    template_name="delete.html"
    success_url=reverse_lazy("show")
