from django.shortcuts import render, redirect
from django.http import HttpRequest
from accounts.models import HumanResourceProfile, User
from .models import Comment, Appointment
# Create your views here.

def home(request:HttpRequest):
    '''function to view the home page '''

    return render(request, "BeReady/base.html")


def update_profile(request:HttpRequest, user_id:int):
    '''function to update HR profile'''
    try:
        HR = User.objects.get(id=user_id)
    except:
        return render(request , "blogApp/not_found.html")

    if request.method == "POST":
        HR.first_name = request.POST.get("first_name")
        HR.last_name = request.POST.get("last_name")
        HR.username = request.POST.get("username")
        HR.email = request.POST.get("email")
        HR.password = request.POST.get("password")
        HR.price = request.POST.get("price")
        HR.card_number = request.POST.get("card_number")
        HR.desceiption = request.POST.get("desceiption")
        HR.image = request.POST.get("image")
        HR.save()

        return redirect("BeReady:view_hr")

    return render(request, "BeReady/update_profile.html",{"HR" : HR})


def profile(request:HttpRequest):
    '''function to view HR profile'''
    try:
        user_id : User = request.user.id
        HR = User.objects.get(id=user_id)
        HR_profile = HumanResourceProfile.objects.get(user_id=user_id)
        appointments = Appointment.objects.filter(HR = HR_profile)
    except:
         return render(request ,"BeReady/not_found.html")
        
    return render(request, "BeReady/HR_profile.html",{ "HR":HR,'appointments':appointments})


def view_hr(request:HttpRequest):
    '''function to view all human resources'''
    if "search" in request.GET:
        HRs = User.objects.filter(first_name__contains=request.GET["search"]) 
    else:
        HRs = User.objects.filter(humanresourceprofile__group="HR")

    return render(request, "BeReady/view_hr.html", {"HRs" : HRs})

    
def HR_detail(request:HttpRequest, user_id : int):
    '''function to view the human resources profile  '''
    try:
        HR = User.objects.get(id=user_id)
        HR_profile = HumanResourceProfile.objects.get(user_id=user_id)
        comments = Comment.objects.filter(HR = HR_profile)
    except:
        return render(request ,"BeReady/not_found.html")
 
    return render(request, "BeReady/HR_detail.html", {"HR" : HR,"comments":comments})


def add_comment(request: HttpRequest, user_id : int):
    '''function to make the user add comment on The human resources'''

    try:
        HR = User.objects.get(id=user_id)
        user : User = request.user
    except:
        return render(request , "BeReady/not_found.html")

    if not (user.is_authenticated):
        return redirect("accounts:login_user")

    if request.method == "POST":
        new_comment = Comment(HR=HR.humanresourceprofile,user=user,content=request.POST["content"])
        new_comment.save()

    return redirect("BeReady:HR_detail", HR.id)


def appointment(request:HttpRequest, user_id : int):
    '''function to view the appoinment page'''

    try:
        HR = User.objects.get(id=user_id)
    except:
        return render(request , "BeReady/not_found.html")

    return render(request, "BeReady/appointment.html",{'HR': HR})


def add_appointment(request: HttpRequest, user_id : int):
    '''function to make the user add comment on The human resources'''
    
    '''
    appointments = Appointment.objects.filter(HR = HR_profile)
            previous_appointments : list = []
            for appoinment in appointments:
                print("#######################",appoinment.appointment_datetime)
                previous_appointments.append(appoinment.appointment_datetime)
            print("#######################",previous_appointments)
            print("@@@@@@@@@@@@@@@@@@@@@@@",new_appointment.appointment_datetime)
    '''
    try:
        HR = User.objects.get(id=user_id)
        user : User = request.user

    except:
        return render(request , "BeReady/not_found.html")

    if not (user.is_authenticated):
        return redirect("accounts:login_user")

    if request.method == "POST":
        new_appointment = Appointment(HR=HR.humanresourceprofile,user=user,desceiption=request.POST.get("desceiption"),appointment_datetime=request.POST.get("appointment_datetime"))
        new_appointment.save()

    return redirect("BeReady:HR_detail", HR.id)


def about(request:HttpRequest):
    '''function to view the about page '''

    return render(request, "BeReady/about.html")


def contact(request:HttpRequest):
    '''function to view the contact page '''

    return render(request, "BeReady/contact.html")
