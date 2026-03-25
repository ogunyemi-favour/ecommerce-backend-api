from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CartView,
    AddToCartView,
    RemoveFromCartView,
    CreateOrderView,
    UserOrdersView,
)
urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),

    path('cart/', CartView.as_view()),
    path('cart/add/', AddToCartView.as_view()),
    path('cart/remove/', RemoveFromCartView.as_view()),

    path('orders/create/', CreateOrderView.as_view()),
    path('orders/', UserOrdersView.as_view()),
]