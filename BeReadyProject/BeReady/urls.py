from django.urls import path
from . import views

app_name = "BeReady"

urlpatterns = [
    path("", views.home, name="home"),
    path("HR/", views.view_hr, name="view_hr"),
    path("Profile/", views.profile, name="profile"),
    
]