from django.urls import path

from .views import (collect_list, get_collect_list, get_sub_detial,
                    collect_create, post_collect, get_collect_details,
                    submit_collect, collect_payview,
                    config_edit, post_config,
                    category_list, get_categories, get_category_by_id,
                    post_category, delete_category, get_col_detail, get_col_total)

urlpatterns = [
    path('collect/list', collect_list, name="collect_list"),

    path('collect/getcoldetail', get_col_detail, name="get_col_tail"),  # 打印报表之获取详细
    path('collect/getcoltotal', get_col_total, name="get_col_total"),  # 打印报表之打印信息

    path('getcollectlist', get_collect_list, name="get_collect_list"),
    path('getsubdetail', get_sub_detial, name="get_sub_detial"),
    path('collect/create', collect_create, name="collect_create"),
    path('postcollect', post_collect, name="post_collect"),
    path('submitcollect', submit_collect, name="submit_collect"),
    path('collect/details', get_collect_details, name='get_collect_details'),
    path('collect/pay', collect_payview, name='collect_payview'),

    path('config', config_edit, name="config_edit"),
    path('postonfig', post_config, name="post_config"),

    path('category/list',category_list, name="category_list" ),
    path('categories',get_categories, name="get_categories" ),
    path('category/<int:id>',get_category_by_id, name="get_category_by_id"),
    path('postcategory', post_category, name="post_category"),
    path('delcategory', delete_category, name="delete_category"),
]