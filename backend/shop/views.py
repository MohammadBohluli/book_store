from . import models
from rest_framework import viewsets
from . import serializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerilizer
