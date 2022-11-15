from django.shortcuts import render, redirect
from django.http import HttpRequest
from accounts.models import HumanResourceProfile, User
from .models import Comment
# Create your views here.

def home(request:HttpRequest):
    '''function to view the home page '''

    return render(request, "BeReady/base.html")


def view_hr(request:HttpRequest):
    '''function to view all human resources'''

    HRs = User.objects.filter(humanresourceprofile__group="HR")


    return render(request, "BeReady/view_hr.html", {"HRs" : HRs})

    
def profile_detail(request:HttpRequest, user_id : int):
    '''function to view the human resources profile  '''

    try:
        HR = User.objects.get(id=user_id)
        HR_profile = HumanResourceProfile.objects.get(user_id=user_id)
        comments = Comment.objects.filter(HR = HR_profile)
    except:
        return render(request , "blogApp/not_found.html")
 
    return render(request, "BeReady/profile.html", {"HR" : HR,"HRp":HR_profile, "comments":comments})
    

def add_comment(request: HttpRequest, user_id : int):
    '''function to make the user add comment on The human resources'''

    try:
        HR = User.objects.get(id=user_id)
        user : User = request.user
    except:
        return render(request , "blogApp/not_found.html")

    if not (user.is_authenticated):
        return redirect("accounts:login_user")

    if request.method == "POST":
        new_comment = Comment(HR=HR.humanresourceprofile,user=user,content=request.POST["content"])
        new_comment.save()

    return redirect("BeReady:profile_detail", HR.id)


