from django.urls import path

from .views import (product_list, get_products, post_product, del_product, create_barcode,
                    storage_enter,)

urlpatterns = [
    path('product/list', product_list, name="product_list"),
    path('getproducts', get_products, name="get_products"),
    path('postproduct', post_product, name="post_product"),
    path('delproduct', del_product, name="del_product"),
    path('createbarcode', create_barcode, name="create_barcode"),

    path("enter", storage_enter, name="storage_enter"),
]