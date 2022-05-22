import graphene
from .types import ItemType, AddItemInput, UpdateItemInput, ShipmentType, AddShipmentInput, UpdateShipmentInput
from items.models import Item, Shipment

class MutationPayload(graphene.ObjectType):
    """
    Object that defines status fields used in all mutations.

    Fields:
        Ok (Boolean): True/False value of whether the action was completed
        Errors (List): List of errors generated
    """
    ok = graphene.Boolean(required=True)
    errors = graphene.List(graphene.String, required=True)

    def resolve_ok(self, info):
        return len(self.errors or []) == 0

    def resolve_errors(self, info):
        return self.errors or []

class AddItem(MutationPayload, graphene.Mutation):
    """GraphQL mutation to create an Item object from ItemInput.

        Args:
            input (AddItemInput)

        Returns:
            ItemType: An Item object
            Boolean: True/False value of whether the object was deleted
            List: List of errors
    """
    class Arguments:
        input = AddItemInput(required=True)

    item = graphene.Field(ItemType)

    def mutate(self, parent, input):
        errors = []
        if not input.is_valid():
            errors.append("Invalid Location. Must be in list: 'Los Angeles' (CA), 'Philadelphia' (PA), 'Portland' (OR), 'Chicago' (IL), 'Miami' (FL)")

        if not errors:
            _item = Item.objects.create(**input)
            return AddItem(item=_item, errors=errors)
        return AddItem(errors=errors)

class DeleteItem(MutationPayload, graphene.Mutation):
    """GraphQL mutation to delete an existing Item object by ID.

        Args:
            id (graphene.ID): ID of Item object

        Returns:
            Boolean: True/False value of whether the object was deleted
            List: List of errors 
    """
    class Arguments:
        id = graphene.ID()
    
    def mutate(self, info, id):
        errors = []
        try:
            Item.objects.get(id=id)
        except Item.DoesNotExist:
            errors.append('Invalid item ID. Item not found.')

        if not errors:
            _item = Item.objects.get(id=id)
            _item.delete()
        return DeleteItem(errors=errors)

class UpdateItem(MutationPayload, graphene.Mutation):
    """GraphQL mutation to update Item object by ID from UpdateItemInput.

        Args:
            id (graphene.ID): ID of Item object
            input (UpdateItemInput)

        Returns:
            ItemType: An Item object
            Boolean: True/False value of whether the action was completed
            List: List of errors generated    
    """
    class Arguments:
        id = graphene.ID()
        input = UpdateItemInput(required=True)

    item = graphene.Field(ItemType)
    
    def mutate(self, info, id, input):
        errors = []
        try:
            item = Item.objects.get(id=id)
        except Item.DoesNotExist:
            errors.append('Invalid item ID. Item not found.')
        if not input.is_valid():
            errors.append("Invalid Location. Must be in list: 'Los Angeles' (CA), 'Philadelphia' (PA), 'Portland' (OR), 'Chicago' (IL), 'Miami' (FL)")

        if not errors:
            _item = Item.objects.get(id=id)
            for k, v in input.items():
                setattr(_item, k, v)
            _item.save()
            return UpdateItem(item=_item, errors=errors)
        return UpdateItem(errors=errors)

class AddShipment(MutationPayload, graphene.Mutation):
    """GraphQL mutation to create a Shipment from AddShipmentInput. Items associated with a Shipment are not distinct.

        Args:
            itemIds ([Int]): Required list of item object IDs
            input (AddShipmentInput)

        Returns:
            ShipmentType: A Shipment object
            Boolean: True/False value of whether the object was deleted
            List: List of errors
    """
    class Arguments:
        itemIds = graphene.List(graphene.Int, required=True)
        input = AddShipmentInput(required=True)

    shipment = graphene.Field(ShipmentType)
    
    def mutate(self, info, itemIds, input):
        errors = []
        if itemIds and len(itemIds) != len(Item.objects.filter(id__in=itemIds)):
            errors.append(f'Invalid item(s) ID.')
        elif not input.is_valid():
            errors.append("Invalid Location. Must be in list: 'Los Angeles' (CA), 'Philadelphia' (PA), 'Portland' (OR), 'Chicago' (IL), 'Miami' (FL)")

        if not errors:
            _shipment = Shipment.objects.create()
            _item_list = Item.objects.filter(id__in=itemIds)
            Item.objects.filter(id__in=itemIds).update(**input)
            _shipment.items.add(*_item_list)
            return AddShipment(shipment=_shipment, errors=errors)
        return AddShipment(errors=errors)

class DeleteShipment(MutationPayload, graphene.Mutation):
    """GraphQL mutation to delete Shipment by ID. Deleting a Shipment does not delete the associated Items.

        Args:
            id (graphene.ID): ID of Shipment object

        Returns:
            Boolean: True/False value of whether the object was deleted
            List: List of errors generated
    """
    class Arguments:
        id = graphene.ID()
    
    def mutate(self, info, id):
        errors = []
        try:
            Shipment.objects.get(id=id)
        except Shipment.DoesNotExist as e:
            errors.append("Invalid shipment ID. Shipment not found.")

        if not errors:
            _shipment = Shipment.objects.get(id=id)
            _shipment.delete()
        return DeleteShipment(errors=errors)

class UpdateShipment(MutationPayload, graphene.Mutation):
    """GraphQL mutation to update Shipment object by ID from UpdateShipmentInput.

        Args:
            itemIds ([Int]): Optional list of item object IDs. If not passed, all items associated with shipment will be updated.
            input (UpdateShipmentInput)

        Returns:
            ShipmentType: A Shipment object
            Boolean: True/False value of whether the object was deleted
            List: List of errors generated
    """
    class Arguments:
        id = graphene.ID(required=True)
        itemIds = graphene.List(graphene.Int, required=False)
        input = UpdateShipmentInput(required=True)

    shipment = graphene.Field(ShipmentType, required=False)
    
    def mutate(self, info, id, input, itemIds=None):
        errors = []
        try:
            shipment = Shipment.objects.get(id=id)
            if itemIds:
                shipment.items.filter(id__in=itemIds)
        except (Shipment.DoesNotExist, Item.DoesNotExist):
            errors.append("Shipment or item does not exist.")
            return UpdateShipment(errors=errors)

        _shipment = Shipment.objects.get(id=id)
        _items = _shipment.items.all()
        if itemIds and len(itemIds) != len(_shipment.items.filter(id__in=itemIds)):
            errors.append(f'Invalid item(s) ID.')
        elif not input.is_valid():
            errors.append("Invalid Location. Must be in list: 'Los Angeles' (CA), 'Philadelphia' (PA), 'Portland' (OR), 'Chicago' (IL), 'Miami' (FL)")

        if not errors:
            if not itemIds:
                _items = _shipment.items.all().update(**input)
                _shipment.save()
                return UpdateShipment(shipment=_shipment, errors=errors)
            else:
                _input_items = _shipment.items.filter(id__in=itemIds).update(**input)
                _shipment.save()
                return UpdateShipment(shipment=_shipment, errors=errors)
        return UpdateShipment(errors=errors)
            

class Mutation(graphene.ObjectType):
    add_item = AddItem.Field()
    delete_item = DeleteItem.Field()
    update_item = UpdateItem.Field()
    add_shipment = AddShipment.Field()
    delete_shipment = DeleteShipment.Field()
    update_shipment = UpdateShipment.Field()