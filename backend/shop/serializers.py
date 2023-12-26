from rest_framework import serializers
from . import models


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = ["id", "name"]


class BookSerilizer(serializers.ModelSerializer):
    # publisher = PublisherSerializer(read_only=True)

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
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.Category
        fields = ["id", "name", "slug"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ["id"]
