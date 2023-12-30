from rest_framework import serializers
from django.db import transaction
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


class AddCartItemSerilizer(serializers.ModelSerializer):
    book_id = serializers.IntegerField()

    def validate_book_id(self, value):
        if not models.Book.objects.filter(pk=value).exists():
            raise serializers.ValidationError("No book with he given ID was found.")
        return value

    def save(self, **kwargs):
        cart_id = self.context["cart_id"]
        book_id = self.validated_data["book_id"]
        quantity = self.validated_data["quantity"]
        try:
            cart_item = models.CartItem.objects.get(cart_id=cart_id, book_id=book_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except models.CartItem.DoesNotExist:
            models.CartItem.objects.create(cart_id=cart_id, **self.validated_data)
        return self.instance

    class Meta:
        model = models.CartItem
        fields = ["id", "book_id", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price_cart = serializers.SerializerMethodField()

    class Meta:
        model = models.Cart
        fields = ["id", "items", "total_price_cart"]

    def get_total_price_cart(self, cart: models.Cart):
        items = cart.items.all()
        result = sum([item.quantity * item.book.price for item in items])
        return result


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ["quantity"]


class OrderItemSerializer(serializers.ModelSerializer):
    book = SimpleBookSerilizer()

    class Meta:
        model = models.OrderItem
        fields = ["id", "book", "quantity", "unit_price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = models.Order
        fields = ["id", "customer", "placed_at", "payment_status", "items"]


class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data["cart_id"]
            customer = models.Customer.objects.get(user_id=self.context["user_id"])
            order = models.Order.objects.create(customer=customer)
            cart_items = models.CartItem.objects.filter(cart_id=cart_id)

            order_item = [
                models.OrderItem(
                    order=order,
                    book=item.book,
                    quantity=item.quantity,
                    unit_price=item.book.price,
                )
                for item in cart_items
            ]

            models.OrderItem.objects.bulk_create(order_item)
            models.Cart.objects.filter(pk=cart_id).delete()
