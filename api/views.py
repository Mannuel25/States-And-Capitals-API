from rest_framework import viewsets, permissions
from .serializers import StateSerializer, UserSerializer
from .models import States
from django.contrib.auth import get_user_model

class StatesViewSet(viewsets.ModelViewSet):
    queryset = States.objects.all()
    serializer_class = StateSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]
