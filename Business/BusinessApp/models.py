from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# import the standard Django Model
# from built-in library
           
class Business(models.Model):
    # fields of the model
    organisation_name = models.CharField(max_length = 200)
    address = models.TextField()
    owner_info = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_size = models.IntegerField()
