from . import models
from django_filters import rest_framework as filters


class BookFilter(filters.FilterSet):
    class Meta:
        model = models.Book
        fields = {"title": ["contains"], "price": ["gte", "lte"]}
