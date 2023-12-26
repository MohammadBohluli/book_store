from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from review.views import ReviewViewSet
from . import views


router = DefaultRouter()

router.register("books", views.BookViewSet, basename="book")
router.register("categories", views.CategoryViewSet, basename="category")

books_router = routers.NestedSimpleRouter(router, "books", lookup="book")
books_router.register("reviews", ReviewViewSet, basename="book-reviews")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(books_router.urls)),
]
