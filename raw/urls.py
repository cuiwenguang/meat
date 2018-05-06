from django.urls import path

from .views import (collect_list, get_collect_list, get_sub_detial,
                    collect_create, post_collect, get_collect_details,
                    config_edit, post_config,
                    category_list, get_categories, get_category_by_id,
                    post_category, delete_category)

urlpatterns = [
    path('collect/list', collect_list, name="collect_list"),
    path('getcollectlist', get_collect_list, name="get_collect_list"),
    path('getsubdetail', get_sub_detial, name="get_sub_detial"),
    path('collect/create', collect_create, name="collect_create"),
    path('postcollect', post_collect, name="post_collect"),
    path('collect/details', get_collect_details, name='get_collect_details'),

    path('config', config_edit, name="config_edit"),
    path('postonfig', post_config, name="post_config"),

    path('category/list',category_list, name="category_list" ),
    path('categories',get_categories, name="get_categories" ),
    path('category/<int:id>',get_category_by_id, name="get_category_by_id"),
    path('postcategory', post_category, name="post_category"),
    path('delcategory', delete_category, name="delete_category"),
]