import datetime
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import RawConfig, Category, CollectInfo, Customer, CollectDetail, get_sg_no


def config_edit(request):
    config = RawConfig.objects.first()
    return render(request, 'raw/config.html', {"config":config})


def post_config(request):
    if request.method != "POST":
        return JsonResponse({"code": 403})

    config = RawConfig.objects.first()
    if config is None:
        config = RawConfig()
    config.default_number = request.POST.get("default_number")
    config.default_tare = request.POST.get("default_tare")
    config.unit_of_weight = request.POST.get("unit_of_weight")
    config.unit_of_number = request.POST.get("unit_of_number")
    config.save()
    return JsonResponse({"code":200, "message": "配置信息保存成功"})


def category_list(request):
    return render(request, "raw/category.html")


def get_categories(request):
    categories = Category.get_categories()
    return JsonResponse({"code":200, "data": [c.to_dict() for c in categories]})


def get_category_by_id(request, id):
    category = Category.objects.get(id=id)
    return JsonResponse({"code": 200, "data": category.to_dict()})


def post_category(request):
    if request.method != "POST":
        return JsonResponse({"code": 403})

    id = request.POST.get("id")
    if int(id) == 0:
        item = Category()
    else:
        item = Category.objects.get(id=id)
    item.name = request.POST.get("name")
    item.default_price = request.POST.get("price")
    item.save()

    return JsonResponse({"code":200, "message": "创建品种完成"})


@csrf_exempt
def delete_category(request):
    if request.method != "POST":
        return JsonResponse({"code": 403})
    id = request.POST.get("id", 0)
    item = Category.objects.get(id=id)
    item.state = 0
    item.save()
    return JsonResponse({"code": 200, "message": "删除成功"})


def collect_create(request):
    config = RawConfig.objects.first()
    categories = Category.get_categories()
    id = request.GET.get("id", 0)
    try:
        model = CollectInfo.objects.get(id=id)
    except:
        model = CollectInfo(sg_datetime=datetime.datetime.now())

    return render(request, 'raw/collect_create.html',
                  {
                      "config": config,
                      "categories": categories,
                      "model": model
                  })


def collect_list(request):
    return render(request, 'raw/collect_list.html')


def get_collect_list(request):
    offset = request.GET.get("offset", 0)
    limit = request.GET.get("limit", 10)
    data = CollectInfo.search(int(offset), int(limit))
    return JsonResponse(data)


def post_collect(request):
    id = request.POST.get("id", 0)
    if int(id) > 0:
        model = CollectInfo.objects.get(id=id)
    else:
        model = CollectInfo()
        model.sg_no = get_sg_no()

    id_card = request.POST.get("id_card", '')
    if len(id_card) > 14:
        cust_name = request.POST.get("cust_name")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        customer = Customer.save_and_get(id_card,
                                         mobile=mobile,
                                         cust_name=cust_name,
                                         address=address)
    else:
        customer = None

    model.customer = customer
    model.user = request.user
    model.save()

    detail = CollectDetail()
    detail.category_id = request.POST.get("category")
    detail.collect_info = model
    detail.number = request.POST.get("number")
    detail.weight = request.POST.get("weight")
    detail.p_weight = request.POST.get("p_weight")
    detail.m_weight = request.POST.get("m_weight")
    detail.price = request.POST.get("price")
    detail.save()
    model.update_total_fields()

    return JsonResponse({"code": 200, "message": "称重记录保存成功", "data": model.to_dict()})


def get_collect_details(request):
    id = request.GET.get("id", 0)
    details = CollectDetail.objects.filter(collect_info_id=id)
    return JsonResponse({"code": 200, "data": [d.to_dict() for d in details]})


def get_sub_detial(request):
    id = request.GET.get("id", 0)
    items = CollectDetail.objects.filter(collect_info_id=id)
    result = [d.to_dict() for d in items]
    return render(request, 'raw/partail_detail.html', {"items": result})

