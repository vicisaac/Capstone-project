
# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu  # Import the Menu model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']  # Specify the fields to serialize

