from django.shortcuts import render
from django.http import HttpRequest
from accounts.models import HumanResourceProfile, User

# Create your views here.

def home(request:HttpRequest):

    return render(request, "BeReady/base.html")


def view_hr(request:HttpRequest):
    HRs = HumanResourceProfile.objects.all()

    print('')

    return render(request, "BeReady/view_hr.html", {"HRs" : HRs})

    return render(request, "BeReady/view_hr.html")


def profile(request:HttpRequest):

    return render(request, "BeReady/profile.html")



