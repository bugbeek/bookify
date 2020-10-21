from django.db import models
from phone_field import PhoneField

# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    Contact = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length = 254)
