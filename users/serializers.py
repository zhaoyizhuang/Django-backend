from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    """
    This class defines serializers which is the representation of our model
    in JSON format and convert object instances to a more transferable
    format. This will simplify the parsing of data for our API.
    """
    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "phone_number", "email", "role"]
