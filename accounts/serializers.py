from django.db.models import fields
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from .models import NewUser
from rest_framework import serializers

from accounts import models

class NewUserSerializer (BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = NewUser
        fields = '__all__'
