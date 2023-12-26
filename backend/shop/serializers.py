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
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = models.CartItem
        fields = ["id", "book", "quantity", "total_price"]

    def get_total_price(self, cart_item: models.CartItem):
        return cart_item.quantity * cart_item.book.price


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)
    total_price_cart = serializers.SerializerMethodField()

    class Meta:
        model = models.Cart
        fields = ["id", "items", "total_price_cart"]

    def get_total_price_cart(self, cart: models.Cart):
        items = cart.items.all()
        result = sum([item.quantity * item.book.price for item in items])
        return result
