from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home(request:HttpRequest):

    return render(request, "BeReady/base.html")


def view_hr(request:HttpRequest):

    return render(request, "BeReady/view_hr.html")

def add_hr(request:HttpRequest):

    return render(request, "BeReady/add_HR.html")



