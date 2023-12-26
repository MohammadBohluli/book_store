from . import models
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from . import paginations
from . import filters
from . import serializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerilizer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.BookFilter
    pagination_class = paginations.CustomPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CartViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Cart
    serializer_class = serializers.CartSerializer
