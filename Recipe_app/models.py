import datetime
import os
from django.contrib.auth.models import User
from django.db import models



def getFileName(request,filename):
    now_time=datetime.detetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)


class List(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name


class FoodType(models.Model):
    food_type = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.food_type


class Recipes(models.Model):
    Recipe = models.ForeignKey(List, on_delete=models.SET_NULL, null=True, blank=True)
    food_type = models.ForeignKey(FoodType, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=getFileName,null=True, blank=False)
    cooking_time = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    saved_by = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

    def __str__(self):
        return self.user



class UserFeedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"





