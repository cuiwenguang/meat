from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout as sys_logout


def logout(request):
    sys_logout(request)
    return redirect(index)


@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def nav(request):
    modules = [
        {
            "id": 1,
            "name": "收购",
            "url": "collect",
            "icon": "fa-tachometer",
            "lable": "raw",
            "model": "collectinfo",
            "parent": 0,
            "children": [
                {
                    "name": "收购称重",
                    "url": "/raw/collect/create",
                    "icon": "fa-tachometer",
                    "lable": "raw",
                    "model": "collectinfo",
                    "parent": 1,
                },
                {
                    "name": "收购台账",
                    "url": "/raw/collect/list",
                    "icon": "fa-table",
                    "lable": "raw",
                    "model": "collectinfo",
                    "parent": 1,
                },
                {
                    "name": "收购结算",
                    "url": "/raw/collect/list",
                    "icon": "fa-table",
                    "lable": "raw",
                    "model": "collectinfo",
                    "parent": 1,
                },
                {
                    "name": "收购品种管理",
                    "url": "/raw/collect/list",
                    "icon": "fa-table",
                    "lable": "raw",
                    "model": "collectinfo",
                    "parent": 1,
                },
                {
                    "name": "收购参数设置",
                    "url": "/raw/collect/list",
                    "icon": "fa-table",
                    "lable": "raw",
                    "model": "collectinfo",
                    "parent": 1,
                },
            ]
        },
        {
            "id": 2,
            "name": "加工",
            "icon": "fa-asterisk",
            "url": "production",
            "label": "raw",
            "model": "collectinfo",
            "parent": 0,
            "children": [
                {
                    "name": "排酸称重",
                    "url": "#",
                    "icon": "fa-table",
                    "label": "raw",
                    "model": "collectinfo",
                    "parent": 2,
                },
                {
                    "name": "排酸台账",
                    "url": "#",
                    "icon": "fa-table",
                    "label": "raw",
                    "model": "collectinfo",
                    "parent": 2,
                }
            ]
        },
        {
            "id": 3,
            "name": "产品",
            "icon": "fa-barcode",
            "url": "inventory",
            "label": "",
            "model": "",
            "parent": 0,
            "children": [
                {
                    "name": "基本信息",
                    "url": "",
                    "icon": "",
                    "label": "",
                    "model": "",
                    "parent": 3,
                },
                {
                    "name": "商品入库",
                    "url": "",
                    "icon": "",
                    "label": "",
                    "model": "",
                    "parent": 3,
                },
                {
                    "name": "商品出库",
                    "url": "",
                    "icon": "",
                    "label": "",
                    "model": "",
                    "parent": 3,
                }
            ],
        },
        {
            "id": 4,
            "name": "统计分析",
            "icon": "fa-th",
            "parent": 0,
        },
        {
            "id": 5,
            "name": "系统管理",
            "icon": "fa-user",
            "parent": 0,
            "children": [

            ]
        }
    ]
    return render(request, 'nav.html', {"modules": modules})