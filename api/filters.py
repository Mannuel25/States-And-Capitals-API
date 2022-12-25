from django_filters import rest_framework as filters
from .models import States

class StatesFilter(filters.FilterSet):
    state = filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model = States
        fields = ['state', 'capital', 'governor', 'slogan','foundation_year','no_of_lgas']