from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    class Languages(models.TextChoices):
        Persian = "fr", _("Persian")
        English = "en", _("English")

    title = models.CharField(max_length=255)
    description = models.TextField()
    isbn = models.CharField(max_length=10, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    num_pages = models.PositiveIntegerField()
    language = models.CharField(
        max_length=2, choices=Languages.choices, default=Languages.English
    )
    category = models.ManyToManyField("Category")
    publisher = models.ForeignKey(
        "Publisher", on_delete=models.CASCADE, related_name="books_publisher"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]

    def __str__(self) -> str:
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}"


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}"
