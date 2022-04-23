from django.db import models

class StatesAndCapitals(models.Model):
    state = models.CharField(max_length=250)
    capital = models.CharField(max_length=250)
    author = models.CharField(max_length=250)

    def __str__(self):
        return self.state
