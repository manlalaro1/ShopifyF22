import graphene
from .types import ItemType
from items.models import Item
import os, requests

class Query(graphene.ObjectType):
    all_items = graphene.List(ItemType)
    item = graphene.Field(ItemType, itemId=graphene.String())

    def resolve_all_items(self, parent):
        """GraphQL query for all Item objects

        Args:
            None

        Returns:
            [Item]: QuerySet of Item objects
        """
        return Item.objects.all()

    def resolve_item(self, parent, itemId):
        """GraphQL query for Item object by ID

        Args:
            None

        Returns:
            Item: An Item object
        """
        print(Item.objects.get(id=itemId))
        return Item.objects.get(id=itemId)