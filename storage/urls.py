from django.urls import path

from .views import (product_list, get_products, post_product,
                    del_product, create_barcode, get_product,
                    storage_enter, post_enter_storage, get_enter_data, delete_enter_storage,
                    order, order_edit, post_order, get_orders, delete_order,
                    get_details, detail_list, customer_search,
                    order_analysis, show_product, edit_product, enter_stat, get_enter_datas, out_stat, get_out_datas,
                    get_order_list, storage_list, loss_list, loss_check,
                    get_bar_code_name,
                    get_order_list, storage_list, loss_list, get_bar_code_name,
                    exchange_list, exchange_edit, exchange_post, exchange_get_details, exchange_all,
                    exchange_detail_list, exchange_check, exchange_delete, loss_post, loss_get_list, loss_get,
                    storage_check_number, cheek_code)

urlpatterns = [
    path('product/list', product_list, name="product_list"),
    path('product/getcode', get_bar_code_name, name="get_bar_code_name"),  # 获取条码名
    # path('product/cheek/code', cheek_code, name="cheek_code"),  # 异步校验产品编号
    path('editproduct', edit_product, name="edit_product"),  # 编辑产品信息
    path('showproduct', show_product, name="update_product"),  # 更新产品信息
    path('getproducts', get_products, name="get_products"),
    path('getproductbycode', get_product, name="get_product"),
    path('postproduct', post_product, name="post_product"),
    path('delproduct', del_product, name="del_product"),
    path('createbarcode', create_barcode, name="create_barcode"),

    path("info", storage_list, name="storage_list"),
    path("enter", storage_enter, name="storage_enter"),
    path("check/number", storage_check_number, name="storage_check_number"),
    path("post_enter", post_enter_storage, name="post_enter_storage"),
    path("enter/delete", delete_enter_storage, name="delete_enter_storage"),
    path("getenterdata", get_enter_data, name="get_enter_data"),
    path("order", order, name="order"),
    path("order/edit", order_edit, name="order_edit"),
    path("order/delete", delete_order, name="delete_order"),
    path("getorders", get_orders, name="get_orders"),
    path("postorder", post_order, name="post_order"),
    path("order/details", get_details, name="get_details"),
    path("order/detail/list", detail_list, name="detail_list"),
    path("order/getorderlist", get_order_list, name="get_order_list"),  # 获取打印报表信息
    path("customer/search", customer_search, name="customer_search"),

    path("enter/stat", enter_stat, name="enter_stat"),  # 入库统计
    path("enter/stat/data", get_enter_datas, name="get_stat_data"),  # 获取入库统计数据

    path("out/stat", out_stat, name="out_stat"),  # 出库库统计
    path("out/stat/data", get_out_datas, name="get_out_data"),  # 获取出库统计数据
    path("out/analysis", order_analysis, name="order_analysis"),

    path("loss/list", loss_list, name="loss_list"),
    path("loss/post", loss_post, name="loss_post"),
    path("loss/get/list", loss_get_list, name="loss_get_list"),
    path("loss/check", loss_check, name="loss_check"),
    path("loss/get", loss_get, name="loss_get"),

    path("exchange/list", exchange_list, name="exchange_list"),
    path("exchange/edit", exchange_edit, name="exchange_edit"),
    path("exchange/post", exchange_post, name="exchange_post"),
    path("exchange/get/details", exchange_get_details, name="exchange_get_details"),
    path("exchange/all", exchange_all, name="exchange_all"),
    path("exchange/detail/list", exchange_detail_list, name="exchange_detail_list"),
    path("exchange/check", exchange_check, name="exchange_check"),
    path("exchange/delete", exchange_delete, name="exchange_delete"),
]