from django.contrib import admin
from .models import Review


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name", "date_created", "book"]


admin.site.register(Review, ReviewAdmin)
