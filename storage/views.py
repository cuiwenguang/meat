from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Product


def product_list(request):
    models = Product.get_all()
    return render(request, 'storage/product_list.html', {"models": models})


def get_products(request):
    items = Product.get_all()
    models = [ m.to_dict() for m in items]
    return JsonResponse({"code": 200, "data": models})


def post_product(request):
    id = request.POST.get("id", 0)
    if id == 0:
        model = Product()
    else:
        model = Product.get(id)
    fields = {
        "name": request.POST.get("name"),
        "standard": request.POST.get("standard"),
        "packing": request.POST.get("packing"),
        "code": request.POST.get("code"),
        "price": request.POST.get("price"),
        "remark": request.POST.get("remark"),
        "state": request.POST.get("state", 1),
    }
    model.update(**fields)
    return JsonResponse({"code":200, "message": "产品信息保存成功"})


def del_product(request):
    id = request.POST.get("id")
    Product.del_product(id)
    return JsonResponse({"code": 200, "message": "产品删除"})


def create_barcode(request):
    ids = request.POST.get("ids")
    val = ids.split(',')
    models = Product.search(id__in = val)
    for m in models:
        m.create_barcode()

    return JsonResponse({"code": 200, "message": "条形码生产完毕"})