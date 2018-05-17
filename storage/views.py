from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Product, EnterStorage, StorageInfo, Customer


def product_list(request):
    models = Product.get_all()
    return render(request, 'storage/product_list.html', {"models": models})


def get_products(request):
    return JsonResponse({"code":200, "data":Product.get_all()})


def post_product(request):
    id = request.POST.get("id", 0)
    if int(id) == 0:
        model = Product()
    else:
        model = Product.get(id)

    model.name = request.POST.get("name")
    model.standard = request.POST.get("standard")
    model.packing = request.POST.get("packing")
    model.code = request.POST.get("code")
    model.price = request.POST.get("price")
    model.remark = request.POST.get("remark")
    model.save()
    model.create_barcode()
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


def get_product(request):
    code = request.GET.get("code")
    model = Product.get_by_code(code)
    return JsonResponse({"code": 200, "data": model.to_dict()})


def storage_enter(request):
    return render(request, 'storage/storage_enter.html')


def get_enter_data(request):
    limit = request.GET.get("limit", 10)
    offset = request.GET.get("offset", 0)
    data = EnterStorage.search(int(limit), int(offset), None)
    return JsonResponse(data)


def post_enter_storage(request):
    """入库"""
    model = EnterStorage()
    model.user = request.user
    model.product_id = request.POST.get("id")
    model.number = int(request.POST.get("number"))
    storage  = StorageInfo()
    storage.enter_storage(model)
    return JsonResponse({"code":200, "message": "入库成功"})


def cancel_enter_storage(request):
    pk = request.GET.get("id")
    StorageInfo.cancel_enter(pk)
    return JsonResponse({"code": 200, "message": "取消入库"})


def order(request):
    return render(request, 'storage/order_list.html')

def order_edit(request):
    products = Product.get_all()
    customer = Customer.get_all()
    return render(request, 'storage/order_edit.html', locals())