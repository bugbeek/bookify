from rest_framework import serializers
from .models import Profile,Books

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','url','firstname','lastname','Contact','email']

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','url','name','descriptions','price']