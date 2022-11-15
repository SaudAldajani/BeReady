from django.shortcuts import render
from django.http import HttpRequest
from accounts.models import HumanResourceProfile, User

# Create your views here.

def home(request:HttpRequest):

    return render(request, "BeReady/base.html")

def profile(request:HttpRequest):

    return render(request, "BeReady/profile.html")

def view_hr(request:HttpRequest):
    HRs = User.objects.filter(humanresourceprofile__group="HR")
    HRp = HumanResourceProfile.objects.all()

    return render(request, "BeReady/view_hr.html", {"HRs" : HRs,"HRp":HRp})

    
def profile_detail(request:HttpRequest, user_id : int):
  
    HR = User.objects.get(id=user_id)
    HRp = HumanResourceProfile.objects.get(user_id=user_id)
    
 
    return render(request, "BeReady/profile.html", {"HR" : HR,"HRp":HRp})



