from rest_framework import viewsets, permissions
from .serializers import StateSerializer, UserSerializer
from .models import States
from django.contrib.auth import get_user_model
from .filters import StatesFilter

class StatesViewSet(viewsets.ModelViewSet):
    queryset = States.objects.all()
    serializer_class = StateSerializer
    filter_class = StatesFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]
