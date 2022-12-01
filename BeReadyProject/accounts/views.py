from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import HumanResourceProfile 

# Create your views here.

def register_user(request : HttpRequest):
    '''function to create a new user'''

    if request.method == "POST":

        new_user = User.objects.create_user(first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),username=request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
        new_user.save()
        return redirect("BeReady:home")
        
    return render(request, "accounts/register.html")
    

def register_human_resource(request : HttpRequest):
    '''function to create a new human resource user'''

    if request.method == "POST":

        new_hr = User.objects.create_user(first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),username=request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
        new_hr.save()

        hr_profile = HumanResourceProfile(user=new_hr, group="HR", desceiption=request.POST.get('desceiption'),price=request.POST.get('price'),card_number=request.POST.get('card_number'),image=request.FILES.get('image', 'default.jfif'))
        hr_profile.save()
        return redirect("BeReady:home")
        
    return render(request, "accounts/hr_register.html")


def login_user(request : HttpRequest):
    '''function to login a user'''

    massage: str = ""
    
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        
        if user:
            login(request, user)
            return redirect("BeReady:home")
        else:
            massage = "User Not Found, Check Your Credentials"

    return render(request, "accounts/login.html", {"msg" : massage})


def logout_user(request: HttpRequest):
    '''function to logout a user'''

    logout(request)

    return redirect("BeReady:home")

    
