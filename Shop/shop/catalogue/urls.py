from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import list_products, product_detail, add_to_cart, cart_detail, remove_from_cart, create_product


app_name = "catalogue"

urlpatterns = [
    path('products/create/', login_required(create_product), name="create_product"),
    path('products/', list_products, name='list_products'),
    path('products/<int:id>/', product_detail, name='product_details'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]
