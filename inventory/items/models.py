from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=100)
    storage_city = models.CharField(max_length=50)

    def __str__(self):
        return self.name