from . import models
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from .permissions import IsAdminOrReadOnly
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
