from collections.abc import Iterable
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from accounts.models import Customer
from uuid import uuid4


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
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}"


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])


class Order(models.Model):
    class PendingStatus(models.TextChoices):
        PAYMENT_STATUS_COMPLETE = "C", _("Complete")
        PAYMENT_STATUS_PENDING = "P", _("Pending")
        PAYMENT_STATUS_FAILED = "F", _("Failed")

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=PendingStatus.choices,
        default=PendingStatus.PAYMENT_STATUS_PENDING,
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="orderitems")
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
