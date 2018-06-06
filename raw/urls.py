from django.urls import path

from .views import (collect_list, get_collect_list, get_sub_detial,
                    collect_create, post_collect, get_collect_details,
                    submit_collect, collect_payview,
                    config_edit, post_config,
                    category_list, get_categories, get_category_by_id,
                    post_category, delete_category, get_col_detail, collect_edit, collect_update,
                    collect_update_info, collect_delcollectinfo, collect_update_customer, stat_list, get_stat_data,
                    collect_analyze, collect_del)

urlpatterns = [
    path('collect/list', collect_list, name="collect_list"),

    path('collect/getcoldetail', get_col_detail, name="get_col_tail"),  # 打印报表之获取详细
    # path('collect/getcoltotal', get_col_total, name="get_col_total"),  # 打印报表之打印信息

    path('collect/edit', collect_edit, name="collect_edit"),  # 编辑信息
    path('collect/del', collect_del, name="collect_del"),  # 删除信息
    path('collect/update', collect_update, name="collect_update"),  # 更新信息
    path('collect/updateInfo', collect_update_info, name="collect_update_info"),  # 更新具体信息
    path('collect/delcollectinfo', collect_delcollectinfo, name="collect_update_customer"),  # 删除收购信息
    path('collect/updatecustomer', collect_update_customer, name="collect_update_customer"),  # 更新客户信息

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

    path('stat', stat_list, name="stat_list"),#跳转页面
    path('getstatdata', get_stat_data, name="get_stat_data"),#获取统计信息
    path('analyze', collect_analyze, name="collect_analyze")
]