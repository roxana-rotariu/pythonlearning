from django.urls import path
from . import views
from .views import ProductListView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/discount/", views.discount_product, name="discount_product"),
]
