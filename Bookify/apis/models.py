from django.db import models
from phone_field import PhoneField
from datetime import datetime



# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    Contact = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.email


#this is upload book model
class Books(models.Model):
    name = models.CharField(max_length= 100)
    price = models.IntegerField()
    descriptions = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name