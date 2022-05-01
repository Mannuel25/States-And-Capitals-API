from rest_framework import viewsets
from .serializers import StateSerializer, UserSerializer
from .models import States
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

class StatesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = States.objects.all()
    serializer_class = StateSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
