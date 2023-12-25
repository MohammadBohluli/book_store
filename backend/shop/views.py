from . import models
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from . import filters
from . import serializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerilizer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.BookFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
