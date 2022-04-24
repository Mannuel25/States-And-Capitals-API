from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import StatesAndCapitals
from .serializers import StateSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
class StateViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = StatesAndCapitals.objects.all()
    serializer_class = StateSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer