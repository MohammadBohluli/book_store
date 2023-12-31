from django.contrib import admin
from . import models


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "price",
        "get_category",
        "publisher",
        "created",
    ]

    @admin.display(description="categoreis")
    def get_category(self, obj):
        res = [category.name for category in obj.category.all()]
        return ", ".join(res)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_display_links = ["name"]
    exclude = ["slug"]


class CartAdmin(admin.ModelAdmin):
    list_display = ["id"]


class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart", "book", "quantity"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["placed_at", "payment_status", "customer"]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "book", "quantity", "unit_price"]


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartItem, CartItemAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)
