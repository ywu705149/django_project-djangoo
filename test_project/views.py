from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def member_profile(request):
    return render(request,"member_profile.html")

def sign_up(request):
    return render(request,"sign_up.html")

def purchase_record(request):
    return render(request,"purchase_record.html")
  
def shopping_cart(request):
    return render(request,"shopping_cart.html")

def save(request):
    return render(request,"save.html")    
   
def category(request):
    return render(request,"category.html")   


def category1(request):
    return render(request,"category1.html")   

