from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Member(models.Model):
    name=models.CharField(max_length=40)
    occupation=models.CharField(max_length=40)
    slogan=models.CharField(max_length=50)
    residence=models.CharField(max_length=50)
    photo =models.ImageField()
    campus=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    hobby=models.CharField(max_length=50)
    age=models.IntegerField()
    nationality=models.CharField(max_length=40)
    primary=models.CharField(max_length=40)
    secondary=models.CharField(max_length=40)
    email=models.EmailField()
    is_male=models.BooleanField(default=True)
    def __str__(self):
        return self . name
    def get_absolute_url(self):
        return reverse('healthp:index')
