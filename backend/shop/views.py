from . import models
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from . import paginations
from . import filters
from . import serializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerilizer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.BookFilter
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = paginations.CustomPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class CartViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Cart
    serializer_class = serializers.CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.AddCartItemSerilizer
        elif self.request.method == "PATCH":
            return serializers.UpdateCartItemSerializer
        return serializers.CartItemSerializer

    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}

    def get_queryset(self):
        return models.CartItem.objects.filter(cart_id=self.kwargs["cart_pk"])


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return models.Order.objects.all()
        customer_id = models.Customer.objects.get(user_id=user.id)
        return models.Order.objects.filter(customer_id=customer_id)
