from graphene_django import DjangoObjectType, DjangoListField
from items.models import Item
from django.db import models
import graphene
import os, requests

class ItemType(DjangoObjectType):
    """
    GraphQL type to represent the Item model from models.Item
    """
    class Meta:
        model = Item
        fields = ("id", "name", "storage_city")

    weather = graphene.String()
    def resolve_weather(self, info):
        api_key = os.getenv("API_KEY")
        city_ids = {"Miami": 4164138, "Los Angeles": 5368361, "Philadelphia": 4560349, "Chicago": 4887398, "Portland": 5746545}
        city_id = city_ids[self.storage_city]
        url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}"
        description = requests.get(url).json()['weather'][0]['description']
        return description
    
class ItemInput(graphene.InputObjectType):
    """
    GraphQL input object of the Item model used in mutations.AddItem
    """
    id = graphene.ID()
    name = graphene.String(required=True)
    storage_city = graphene.String(required=True)

    def is_valid(self):
        cities = ["Los Angeles", "Philadelphia", "Portland", "Chicago", "Miami"]

        if self.storage_city not in cities:
            raise ValueError("Invalid Location. Must be in list: 'Los Angeles' (CA), 'Philadelphia' (PA), 'Portland' (OR), 'Chicago' (IL), 'Miami' (FL)")
        else:
            return True

class UpdateItemInput(graphene.InputObjectType):
    """
    GraphQL input object of the Item model used in mutations.UpdateItem
    """
    id = graphene.ID()
    name = graphene.String(required=False)
    storage_city = graphene.String(required=False)

    def is_valid(self):
        cities = ["Los Angeles", "Philadelphia", "Portland", "Chicago", "Miami"]

        if self.storage_city not in cities:
            raise ValueError("Invalid Location. Must be in list: 'Los Angeles' (CA), 'Philadelphia' (PA), 'Portland' (OR), 'Chicago' (IL), 'Miami' (FL)")
        else:
            return True