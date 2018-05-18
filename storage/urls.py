from django.urls import path

from .views import (product_list, get_products, post_product,
                    del_product, create_barcode, get_product,
                    storage_enter, post_enter_storage, get_enter_data,
                    order, order_edit, post_order, get_orders, get_details,
                     detail_list, customer_search)

urlpatterns = [
    path('product/list', product_list, name="product_list"),
    path('getproducts', get_products, name="get_products"),
    path('getproductbycode', get_product, name="get_product"),
    path('postproduct', post_product, name="post_product"),
    path('delproduct', del_product, name="del_product"),
    path('createbarcode', create_barcode, name="create_barcode"),

    path("enter", storage_enter, name="storage_enter"),
    path("post_enter", post_enter_storage, name="post_enter_storage"),
    path("getenterdata", get_enter_data, name="get_enter_data"),
    path("order", order, name="order"),
    path("order/edit", order_edit, name="order_edit"),
    path("getorders", get_orders, name="get_orders"),
    path("postorder", post_order, name="post_order"),
    path("order/details", get_details, name="get_details"),
    path("order/detail/list", detail_list, name="detail_list"),

    path("customer/search", customer_search, name="customer_search"),
]