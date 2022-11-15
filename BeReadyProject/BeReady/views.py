from django.shortcuts import render, redirect
from django.http import HttpRequest
from accounts.models import HumanResourceProfile, User
from .models import Comment
# Create your views here.

def home(request:HttpRequest):

    return render(request, "BeReady/base.html")

def profile(request:HttpRequest):

    return render(request, "BeReady/profile.html")

def view_hr(request:HttpRequest):
    HRs = User.objects.filter(humanresourceprofile__group="HR")


    return render(request, "BeReady/view_hr.html", {"HRs" : HRs})

    
def profile_detail(request:HttpRequest, user_id : int):
  
    HR = User.objects.get(id=user_id)
    HRp = HumanResourceProfile.objects.get(user_id=user_id)
    comments = Comment.objects.filter(HRp = HRp)
    
 
    return render(request, "BeReady/profile.html", {"HR" : HR,"HRp":HRp, "comments":comments})
    

def add_comment(request: HttpRequest, user_id : int):
    HR = User.objects.get(id=user_id)
    user : User = request.user

    if not (user.is_authenticated):
        return redirect("BeReady:register_user")

    if request.method == "POST":
        new_comment = Comment(HR=HR.humanresourceprofile,user=user,content=request.POST["content"])
        new_comment.save()

    
    return redirect("BeReady:profile_detail", HR.id)



