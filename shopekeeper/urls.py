from django.urls import path
from . import views

urlpatterns = [
    path('add-product', views.add_products, name='add-products'),
    path('products/<str:shopekeeper_id>', views.ListProductsAPI.as_view(), name='list-products')
]
