from rest_framework import viewsets
from .serializers import ReviewSerializer
from .models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs.get("book_pk"))

    def get_serializer_context(self):
        return {"book_id": self.kwargs.get("book_pk")}
