from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from review.views import ReviewViewSet
from accounts.views import CustomerViewSet
from . import views


router = DefaultRouter()

router.register("books", views.BookViewSet, basename="book")
router.register("categories", views.CategoryViewSet, basename="category")
router.register("carts", views.CartViewSet, basename="cart")
router.register("customers", CustomerViewSet, basename="customer")
router.register("orders", views.OrderViewSet, basename="order")

books_router = routers.NestedSimpleRouter(router, "books", lookup="book")
books_router.register("reviews", ReviewViewSet, basename="book-reviews")

cart_router = routers.NestedSimpleRouter(router, "carts", lookup="cart")
cart_router.register("items", views.CartItemViewSet, basename="cart-items")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(books_router.urls)),
    path("", include(cart_router.urls)),
]
