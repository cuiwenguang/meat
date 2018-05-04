"""meat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import login as sys_login
from .views import logout, index, nav

from raw.urls import urlpatterns as raw_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', sys_login, {'template_name': 'login.html'}),
    path('logout/', logout, name="logout"),
    path('', index),
    path('nav', nav),
    re_path('raw/', include(raw_urls)),
]
