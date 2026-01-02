from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# UserViewSet handles CRUD operations for the User model
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Queryset to retrieve all users
    serializer_class = UserSerializer  # Serializer to use for User model