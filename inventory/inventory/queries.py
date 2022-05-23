import graphene
from .types import ItemType, ShipmentType
from items.models import Item, Shipment
import os, requests

class Query(graphene.ObjectType):
    all_items = graphene.List(ItemType)
    item = graphene.Field(ItemType, id=graphene.Int())
    shipment = graphene.Field(ShipmentType, id=graphene.Int())
    all_shipments = graphene.List(ShipmentType)

    def resolve_all_items(self, parent):
        """GraphQL query for all Item objects

        Args:
            None

        Returns:
            [Item]: QuerySet of Item objects
        """
        return Item.objects.all()

    def resolve_item(self, parent, id):
        """GraphQL query for Item object by ID

        Args:
            None

        Returns:
            Item: An Item object
        """
        print(Item.objects.get(id=id))
        return Item.objects.get(id=id)

    def resolve_all_shipments(self, parent):
        """GraphQL query for all Shipment objects

        Args:
            None

        Returns:
            [Shipment]: QuerySet of Shipment objects
        """
        return Shipment.objects.all()
    
    def resolve_shipment(self, parent, id):
        """GraphQL query for Shipment object by ID

        Args:
            None

        Returns:
            Shipment: A Shipment object
        """
        return Shipment.objects.get(id=id)