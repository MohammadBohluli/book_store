from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register("books", views.BookViewSet, basename="books")
router.register("categories", views.CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
