import graphene
from .types import ItemType, ItemInput
from items.models import Item

class AddItem(graphene.Mutation):
    """GraphQL mutation to create an Item object from ItemInput

        Args:
            input (ItemInput): All fields of ItemInput are required.

        Returns:
            ItemType: An Item object
    """
    class Arguments:
        input = ItemInput(required=True)

    item = graphene.Field(ItemType)

    def mutate(self, parent, input=None):
        if input is None:
            return AddItem(item=None)
        _item = Item.objects.create(**input)
        return AddItem(item=_item)

class DeleteItem(graphene.Mutation):
    """GraphQL mutation to delete an existing Item object by ID

        Args:
            itemId (graphene.ID): ID of Item object

        Returns:
            Boolean: True/False value of whether the object was deleted
    """
    class Arguments:
        itemId = graphene.ID()

    deleted = graphene.Boolean()
    
    def mutate(self, info, itemId):
        if Item.objects.get(id=itemId):
            _item = Item.objects.get(id=itemId)
            _item.delete()
            return DeleteItem(deleted=True)
        return DeleteItem(deleted=False)

class Mutation(graphene.ObjectType):
    add_item = AddItem.Field()
    delete_item = DeleteItem.Field()