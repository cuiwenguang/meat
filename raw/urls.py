from django.urls import path

from .views import (collect_create, config_edit, post_config,
                    category_list, get_categories, get_category_by_id,
                    post_category, delete_category)

urlpatterns = [
    path('collect/create', collect_create, name="collect_create"),

    path('config', config_edit, name="config_edit"),
    path('postonfig', post_config, name="post_config"),

    path('category/list',category_list, name="category_list" ),
    path('categories',get_categories, name="get_categories" ),
    path('category/<int:id>',get_category_by_id, name="get_category_by_id"),
    path('postcategory', post_category, name="post_category"),
    path('delcategory', delete_category, name="delete_category"),
]