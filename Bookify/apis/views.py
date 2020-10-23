from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Profile,Books
from .serializers import ProfileSerializer,BooksSerializer

# Create your views here.
class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class BooksView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]