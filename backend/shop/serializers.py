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


class SimpleBookSerilizer(serializers.ModelSerializer):
    """this serializer just for display in CartItemSerializer"""

    class Meta:
        model = models.Book
        fields = ["id", "title", "price"]


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.Category
        fields = ["id", "name", "slug"]


class CartItemSerializer(serializers.ModelSerializer):
    book = SimpleBookSerilizer()

    class Meta:
        model = models.CartItem
        fields = ["id", "book", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)

    class Meta:
        model = models.Cart
        fields = ["id", "items"]
