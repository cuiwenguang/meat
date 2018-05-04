from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import RawConfig, Category


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


def raw_list(request):
    return render(request, 'raw/list.html')


def collect_create(request):
    config = RawConfig.objects.first()
    categories = Category.get_categories()
    return render(request, 'raw/collect_create.html',
                  {
                      "config": config,
                      "categories": categories
                  })


