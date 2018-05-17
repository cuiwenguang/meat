"""
    模块集合
"""

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
                    "name": "收购品种管理",
                    "url": "/raw/category/list",
                    "icon": "fa-table",
                    "lable": "raw",
                    "model": "Category",
                    "parent": 1,
                },
                {
                    "name": "收购参数设置",
                    "url": "/raw/config",
                    "icon": "fa-table",
                    "lable": "raw",
                    "model": "RawConfig",
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
            "name": "库存",
            "icon": "fa-barcode",
            "url": "storage",
            "label": "",
            "model": "",
            "parent": 0,
            "children": [
                {
                    "name": "产品",
                    "url": "/storage/product/list",
                    "icon": "",
                    "label": "",
                    "model": "",
                    "parent": 3,
                },
                {
                    "name": "入库",
                    "url": "/storage/enter",
                    "icon": "",
                    "label": "",
                    "model": "",
                    "parent": 3,
                },
                {
                    "name": "出库记录",
                    "url": "/storage/order",
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
            "url": "system",
            "icon": "fa-user",
            "parent": 0,
            "children": [
                {
                    "id": 501,
                    "name": "用户管理",
                    "url": "/system/user",
                    "label": "",
                    "model": "",
                    "parent": 5,
                },
                {
                    "id": 502,
                    "name": "角色管理",
                    "url": "/system/role",
                    "label": "",
                    "model": "",
                    "parent": 5,
                }
            ]
        }
    ]