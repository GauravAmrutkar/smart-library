from .models import Rack, Shelf


class RackService:
    @staticmethod
    def create_rack(**validated_data):
        return Rack.objects.create(**validated_data)


class ShelfService:
    @staticmethod
    def create_shelf(**validated_data):
        return Shelf.objects.create(**validated_data)
