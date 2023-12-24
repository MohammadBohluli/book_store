from rest_framework import serializers
from . import models


class BookSerilizer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = [
            "id",
            "title",
            "description",
            "isbn",
            "quantity",
            "price",
            "num_pages",
            "language",
            "category",
            "publisher",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["id", "name", "slug"]
