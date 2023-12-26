from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "name", "description", "date_created"]

    def create(self, validated_data):
        book_id = self.context["book_id"]
        return Review.objects.create(book_id=book_id, **validated_data)
