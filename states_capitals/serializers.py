from rest_framework import serializers
from .models import StatesAndCapitals
from django.contrib.auth import get_user_model

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatesAndCapitals
        fields = ('contributor','state', 'capital', 'governor', 'slogan', 
            'establishment_year', 'lgas','no_of_lgas')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username')
