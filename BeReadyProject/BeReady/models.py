from django.db import models
from accounts.models import HumanResourceProfile
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    HR = models.ForeignKey(HumanResourceProfile, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
   

class Appointment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    HR = models.ForeignKey(HumanResourceProfile, on_delete = models.CASCADE)
    desceiption = models.TextField()
    appointment_datetime = models.DateTimeField()
