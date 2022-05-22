from django.db import models
import uuid

class Item(models.Model):
    name = models.CharField(max_length=100)
    storage_city = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Shipment(models.Model):
    items = models.ManyToManyField(Item)