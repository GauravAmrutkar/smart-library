from rest_framework.exceptions import ValidationError

from .models import Publisher


class PublisherValidator:
    @staticmethod
    def validate_unique_name(name):

        if Publisher.objects.filter(name__iexact=name).exists():
            raise ValidationError({"name": "Publisher already exists."})
