import datetime
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import RawConfig, Category, CollectInfo, Customer, CollectDetail, PayInfo, get_sg_no


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


def get_col_detail(request):
    id = request.GET.get("id")
    collect_details = CollectDetail.objects.filter(collect_info_id=id)
    return JsonResponse({"code": 200, "data": [c.to_dict() for c in collect_details]})


def get_col_total(request):
    id = request.GET.get("id")
    info = CollectInfo.objects.get(id=id)
    return JsonResponse({"code": 200, "data": info.to_dict()})

def collect_edit(request):
    id = request.GET.get("id")
    config = RawConfig.objects.first()
    categories = Category.get_categories()
    try:
        model = CollectInfo.objects.get(id=id)
    except:
        model = CollectInfo(sg_datetime=datetime.datetime.now())
    details = CollectDetail.objects.filter(collect_info_id=id)
    return render(request, 'raw/collect_edit.html',
                  {
                      "config": config,
                      "categories": categories,
                      "model": model,
                      "details": details,
                      "collect_info_id": id,
                  })


def collect_update(request):
    id = request.GET.get('id')
    collect_info = CollectDetail.objects.get(id=id)
    return JsonResponse({"code": 200, "data": collect_info.to_dict()})


def collect_update_info(request):
    did = request.GET.get("did")
    collect_info = CollectDetail.objects.get(id=did)
    print(collect_info)
    collect_info.price = request.GET.get("price")
    collect_info.number = request.GET.get("number")
    collect_info.weight = request.GET.get("weight")
    collect_info.p_weight = request.GET.get("p_weight")
    collect_info.m_weight = request.GET.get("m_weight")
    collect_info.category_id = request.GET.get("cg_name")
    collect_info.save()
    return JsonResponse({"code": 200, "data": collect_info.to_dict()})


def collect_delcollectinfo(request):
    id = request.GET.get("did")
    c = CollectDetail.objects.get(id=id)
    c.delete()
    CollectDetail.objects.all()
    return JsonResponse({"code": 200})


def collect_update_customer(request):
    id = request.GET.get("collect_info_id")
    collectInfo = CollectInfo.objects.get(id=id)
    collectInfo.sg_datetime = request.GET.get("sgDatetime")
    customer = Customer.objects.get(id=collectInfo.customer_id)
    customer.cust_name = request.GET.get("custName")
    customer.mobile = request.GET.get('mobile')
    customer.address = request.GET.get('address')
    customer.save()
    return JsonResponse({"code": 200})


def get_collect_list(request):
    offset = request.GET.get("offset", 0)
    limit = request.GET.get("limit", 10)
    date_params = request.GET.get("sgDate", "")
    if len(date_params)>0:
        try:
            date_range = [ datetime.datetime.strptime(dd.strip(), "%Y-%m-%d") for dd in date_params.split('~')]
            date_range[1] = date_range[0] + datetime.timedelta(days=1)
        except:
            date_range = []
    else:
        date_range = []
    query_params = {
        "no": request.GET.get("no", ""),
        "sg_date": date_range,
        "customer": request.GET.get("customer", ""),
        "sg_state": [int(s) for s in request.GET.getlist("sgState", [])],
    }
    data = CollectInfo.search(int(offset), int(limit), **query_params)
    return JsonResponse(data)


def post_collect(request):
    """提交称重明细记录"""
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
    detail.seq = request.POST.get("seq")
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


def submit_collect(request):
    """完成称重并提交"""
    id = request.POST.get("id")
    model = CollectInfo.objects.get(id=id)
    id_card = request.POST.get("id_card")
    cust_name = request.POST.get("cust_name")
    mobile = request.POST.get("mobile")
    address = request.POST.get("address")
    customer = Customer.save_and_get(id_card,
                                     mobile=mobile,
                                     cust_name=cust_name,
                                     address=address)
    model.customer = customer
    model.user = request.user
    model.state = 1
    model.save()

    return JsonResponse({"code": 200, "message": "称重记录保存成功", "data": CollectInfo().to_dict()})


def get_collect_details(request):
    id = request.GET.get("id", 0)
    details = CollectDetail.objects.filter(collect_info_id=id)
    return JsonResponse({"code": 200, "data": [d.to_dict() for d in details]})


def get_sub_detial(request):
    id = request.GET.get("id", 0)
    items = CollectDetail.objects.filter(collect_info_id=id)
    result = [d.to_dict() for d in items]
    return render(request, 'raw/partail_detail.html', {"items": result})


def collect_payview(request):
    if request.method == "GET":
        id = request.GET.get("id")
        model = CollectInfo.objects.get(id=id)
        money = model.total_price - PayInfo.get_pay_sum(id)
        today_model = CollectInfo.objects.filter(sg_datetime__gte=datetime.date.today(), state__range=[1, 2])
        details = PayInfo.objects.filter(collect_info_id=id)
        return render(request, 'raw/pay_detail.html', locals())
    else:
        id = request.POST.get("id")
        money = float(request.POST.get("money", 0))
        remark = request.POST.get("remark", '')
        pay_model = PayInfo(pay_money=money, create_at=datetime.datetime.now(),
                            collect_info_id=id, user=request.user,
                            remark=remark)

        model = CollectInfo.objects.get(id=id)

        if money + PayInfo.get_pay_sum(id) == model.total_price:
            model.state = 3
        elif money + PayInfo.get_pay_sum(id) < model.total_price:
            model.state = 2
        else :
            return JsonResponse({"code": 410})

        pay_model.save()
        model.save(update_fields=['state',])
        return HttpResponseRedirect("/raw/collect/pay?id="+id)


def stat_list(request):
    return render(request, 'raw/collect_stat.html')


def get_stat_data(request):
    begin_data = request.GET.get("beginDate")  # 2018-05-01 00:00:00
    end_data = request.GET.get("endDate")  # 2018-05-01 23:59:59
    data = CollectInfo.get_stat_data(begin_data, end_data)
    return JsonResponse({"code": 200, "data": data})
