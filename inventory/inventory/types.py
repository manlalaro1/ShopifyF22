from graphene_django import DjangoObjectType, DjangoListField
from items.models import Item, Shipment
from django.db import models
import graphene
import os, requests

class ItemType(DjangoObjectType):
    """
    GraphQL type to represent the Item model
    """
    class Meta:
        model = Item
        fields = ("id", "name", "storage_city", "quantity")

    weather = graphene.String()
    def resolve_weather(self, info): # method called during each Item GraphQL query
        api_key = os.getenv("API_KEY") # API key pulled from docker-compose.yaml
        city_ids = {
            "Miami": 4164138, 
            "Los Angeles": 5368361, 
            "Philadelphia": 4560349,
             "Chicago": 4887398,
              "Portland": 5746545
            }
        city_id = city_ids[self.storage_city]
        url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}"
        description = requests.get(url).json()['weather'][0]['description']
        return description

class InputPayload(graphene.InputObjectType):
    name = graphene.String()
    storage_city = graphene.String()
    quantity = graphene.Int()
    
    def is_valid(self):
        cities = ["Los Angeles", "Philadelphia", "Portland", "Chicago", "Miami"]

        if self.storage_city not in cities:
            return False
        else:
            return True
    
class AddItemInput(InputPayload, graphene.InputObjectType):
    """
    GraphQL input object of the Item model used in mutations.AddItem
    """
    name = graphene.String(required=True)
    storage_city = graphene.String(required=True)
    quantity = graphene.Int(required=True)

class UpdateItemInput(InputPayload, graphene.InputObjectType):
    """
    GraphQL input object of the Item model used in mutations.UpdateItem
    """
    name = graphene.String(required=False)
    storage_city = graphene.String(required=False)
    quantity = graphene.Int(required=False)

class ShipmentType(DjangoObjectType):
    """
    GraphQL type to represent the Shipment model from models.Shipment
    """
    class Meta:
        model = Shipment
        fields = "__all__"
    
    items = DjangoListField(ItemType)
    def resolve_items(self, info):
        return self.items.all()

class AddShipmentInput(InputPayload, graphene.InputObjectType):
    """
    GraphQL input object of the Shipment model used in mutations.AddShipment
    """
    storage_city = graphene.String(required=True)

class UpdateShipmentInput(InputPayload, graphene.InputObjectType):
    """
    GraphQL input object of the Shipment model used in mutations.UpdateShipment
    """
    itemIds = graphene.List(graphene.Int, required=False)
    storage_city = graphene.String(required=False)
    quantity = graphene.Int(required=False)