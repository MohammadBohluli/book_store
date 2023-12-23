from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(auto_add=True)

    class Meta:
        abstract = True


class Book(TimeStampedModel):
    class Language(models.TextChoices):
        Persian = "fr", _("Persian")
        English = "en", _("English")

    title = models.CharField(max_length=255)
    isbn = models.CharField(
        max_length=10,
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField()
    num_pages = models.PositiveIntegerField()
    language = models.CharField(
        max_length=2, choices=Language, default=Language.English
    )
    category = models.ManyToManyField("Category")
    publisher = models.ManyToManyField("Publisher")

    class Meta:
        ordering = ["created"]

    def __str__(self) -> str:
        return f"{self.title}"


class Category(TimeStampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}"


class Publisher(TimeStampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}"
