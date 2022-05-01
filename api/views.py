from rest_framework import viewsets
from .serializers import StateSerializer, UserSerializer
from .models import States
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from datetime import datetime

class StatesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    all_states = States.objects.all()
    format_today_date = datetime.today().strftime('%Y-%m-%d')
    queryset = []
    for i in all_states:
        # print(i, i.date_created, type(i.date_created))
        if str(i.date_created) == format_today_date:
            queryset.append(i)
    print(queryset)
    serializer_class = StateSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
