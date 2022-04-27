from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import States

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ('id','contributor','state','capital','governor', 
            'slogan','foundation_year','lgas','no_of_lgas')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')