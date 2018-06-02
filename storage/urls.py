from django.urls import path

from .views import (product_list, get_products, post_product,
                    del_product, create_barcode, get_product,
                    storage_enter, post_enter_storage, get_enter_data,
                    order, order_edit, post_order, get_orders, delete_order,
                    get_details, detail_list, customer_search,
                    order_analysis, show_product, edit_product, enter_stat, get_enter_datas, out_stat, get_out_datas)

urlpatterns = [
    path('product/list', product_list, name="product_list"),
    path('editproduct', edit_product, name="edit_product"),  # 编辑产品信息
    path('showproduct', show_product, name="update_product"),  # 更新产品信息
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
    path("order/delete", delete_order, name="delete_order"),
    path("getorders", get_orders, name="get_orders"),
    path("postorder", post_order, name="post_order"),
    path("order/details", get_details, name="get_details"),
    path("order/detail/list", detail_list, name="detail_list"),

    path("customer/search", customer_search, name="customer_search"),

    path("enter/stat", enter_stat, name="enter_stat"),  # 入库统计
    path("enter/stat/data", get_enter_datas, name="get_stat_data"),  # 获取入库统计数据

    path("out/stat", out_stat, name="out_stat"),  # 出库库统计
    path("out/stat/data", get_out_datas, name="get_out_data"),  # 获取出库统计数据
    path("out/analysis", order_analysis, name="order_analysis"),
]