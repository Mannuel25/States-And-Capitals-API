from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

class StatesAndCapitals(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=250)
    capital = models.CharField(max_length=250)
    governor = models.CharField(max_length=250)
    slogan = models.CharField(max_length=250)
    establishment_year = models.CharField(max_length=250)
    lgas = ArrayField(models.CharField(max_length=250), blank=True)
    no_of_lgas = models.CharField(max_length=250, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.state
