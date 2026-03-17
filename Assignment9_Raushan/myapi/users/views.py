#from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# GET + POST
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# GET (single), PUT, DELETE
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
