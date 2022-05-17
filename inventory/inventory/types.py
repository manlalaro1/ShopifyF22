from graphene_django import DjangoObjectType
from items.models import Item
from django.db import models
import graphene

class ItemType(DjangoObjectType):
    """
    GraphQL type to represent the Item model from models.Item
    """
    class Meta:
        model = Item
        fields = ("id", "name", "cityShipped")


class ItemInput(graphene.InputObjectType):
    """
    GraphQL input object of the Item model used in mutations.AddItem
    """
    id = graphene.ID()
    name = graphene.String(required=True)
    cityShipped = graphene.String(required=True)