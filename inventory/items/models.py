from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=100)
    cityShipped = models.TextChoices('cityShipped', 'LAX PHL JFK SFO PDX')

    def __str__(self):
        return self.name