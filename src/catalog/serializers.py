from rest_framework import serializers
from . import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
            "date_of_death"
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = [
            "id",
            "name",
            "author",
            "description",            
        ]