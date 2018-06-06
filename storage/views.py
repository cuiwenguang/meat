import datetime

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Product, EnterStorage, StorageInfo, Customer, Order, OrderDetail,Loss


def product_list(request):
    models = Product.get_all()
    return render(request, 'storage/product_list.html', {"models": models})


def get_products(request):
    data = [d.to_dict() for d in Product.get_all()]
    return JsonResponse({"code": 200, "data":data})


def post_product(request):
    id = request.POST.get("id", 0)
    if int(id) == 0:
        model = Product()
        p_name = request.POST.get("name")
        model.name = request.POST.get("name")
        model.standard = request.POST.get("standard")
        model.packing = request.POST.get("packing")
        model.code = request.POST.get("code")
        model.price = request.POST.get("price")
        model.remark = request.POST.get("remark")
        model.save()
        model.create_barcode()
        product = Product.objects.get(name=p_name)
        print(product)
        info = StorageInfo()
        info.product_id = product.id
        info.save()
        return JsonResponse({"code": 200, "message": "产品信息保存成功"})
    else:
        model = Product.get(id)
        model.name = request.POST.get("name")
        model.standard = request.POST.get("standard")
        model.packing = request.POST.get("packing")
        model.code = request.POST.get("code")
        model.price = request.POST.get("price")
        model.remark = request.POST.get("remark")
        model.save()
        return JsonResponse({"code": 300, "data": model.to_dict()})


def edit_product(request):
    return JsonResponse({"code": 200, "message": "编辑产品信息成功"})


def show_product(request):
    id = request.POST.get('id')
    model = Product.get(id)
    return JsonResponse({"code": 200, "data": model.to_dict()})


def get_bar_code_name(request):
    product_list = Product.objects.filter(state=1)
    return JsonResponse({"code": 200, "data":[c.to_dict() for c in product_list]})


def del_product(request):
    id = request.GET.get("id")
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
    if model is None:
        return JsonResponse({"code": 401, "message": "产品不存在" })
    return JsonResponse({"code": 200, "data": model.to_dict()})


def storage_enter(request):
    products = Product.get_all()
    return render(request, 'storage/storage_enter.html',
                  {"products": products})


def get_enter_data(request):
    limit = request.GET.get("limit", 10)
    offset = request.GET.get("offset", 0)
    condition = {}
    range_data = request.GET.get("rangeDate", '')
    products = request.GET.getlist('products')
    if len(range_data) > 0:
        condition['create_at__range'] = range_data.split(' ~ ')
    if len(products) > 0:
        condition['product_id__in'] = products

    data = EnterStorage.search(int(limit), int(offset), condition)
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


@csrf_exempt
def delete_enter_storage(request):
    pk = request.POST.get("id")
    StorageInfo.cancel_enter(pk)
    return JsonResponse({"code":200, "message": "删除成功"})


def cancel_enter_storage(request):
    pk = request.GET.get("id")
    StorageInfo.cancel_enter(pk)
    return JsonResponse({"code": 200, "message": "取消入库"})


def order(request):
    return render(request, 'storage/order_list.html')


def order_edit(request):
    pk = request.GET.get("id", 0)
    if int(pk) == 0:
        model = Order()
        model.create_at = datetime.datetime.now()
    else:
        model = Order.get(pk)

    products = Product.get_all()
    return render(request, 'storage/order_edit.html', locals())


def post_order(request):
    customer_name = request.POST.get("customer")
    cusotmer = Customer.get_by_name(customer_name)
    if cusotmer is None:
        if len(customer_name)>0:
            cusotmer = Customer(customer_name=customer_name)
            cusotmer.save()
        else:
            None

    hand_user = request.POST.get("hand_user")
    create_at = request.POST.get("create_at")
    money = request.POST.get("money")
    remark = request.POST.get("remark")
    state = request.POST.get("state")
    id = request.POST.get("id")
    if int(id)==0:
        order = Order()
    else:
        order = Order.get(id)
    order.create_at = create_at
    order.customer = cusotmer
    order.user = request.user
    order.hand_user = hand_user
    order.money = money
    order.remark = remark
    order.state = state
    if int(state) == 0:
        detail = OrderDetail()
        detail.order = order
        detail.product_id = request.POST.get("product")
        detail.number = request.POST.get("number")
        detail.remark = ""
    else:
        detail = None
    order.create(detail)

    return JsonResponse({"code": 200, "message": "保存成功", "data": order.to_dict()})


def get_orders(request):
    limit = int(request.GET.get("limit", 10))
    offset = int(request.GET.get("offset", 0))
    date_params = request.GET.get("create_at", "")
    query_params = {}
    if len(date_params) > 0:
        try:
            date_range = [datetime.datetime.strptime(dd.strip(), "%Y-%m-%d") for dd in date_params.split('~')]
            date_range[1] = date_range[0] + datetime.timedelta(days=1)
            query_params["create_at__range"] = date_range
        except:
            pass

    customer = request.GET.get("customer", "")
    if len(customer)>0:
        query_params["customer__customer_name"]=customer
    state = request.GET.getlist("state")
    if len(state):
        query_params["state__in"] = [int(s) for s in state]
    data = Order.search(limit=limit, offset=offset, **query_params)
    return JsonResponse(data)


def get_order_list(request):
    id = request.GET.get("id")
    data = Order.get_order_data(id)
    return JsonResponse({"code": 200, "data": data})


@csrf_exempt
def delete_order(request):
    id = request.POST.get("id")
    Order.remove_at(id)
    return JsonResponse({"code": 200, "message": "删除成功"})


def detail_list(request):
    oid = request.GET.get("id")
    details = Order.details(oid)
    return render(request, "storage/orderdetail_partial.html", locals())


def get_details(request):
    oid = request.GET.get("id")
    details = Order.details(oid)
    return JsonResponse([d.to_dict() for d in details], safe=False)


def customer_search(request):
    keywards = request.GET.get("query", "")
    if len(keywards)==0:
        data = []
    else:
        data = Customer.search(keywards)
    return JsonResponse({"code": 200, "data": [{"id": d["id"], "name":d["customer_name"]} for d in data]})


def order_analysis(request):
    from storage.analysis_utils import to_table_data, to_chart_data

    if request.GET.get("rangeDate"):
        begin_date = request.GET.get("rangeDate").split(' ~ ')[0]
        end_date = request.GET.get("rangeDate").split(' ~ ')[1]
    else:
        dt = datetime.datetime.now()
        begin_date = '-'.join([str(dt.year), str(dt.month), '01'])
        end_date = '-'.join([str(dt.year), str(dt.month), str(dt.day)])
    search_types = request.GET.getlist("selProduct")
    data = Order.get_analysis_by_date(begin_date, end_date, search_types)
    table_data, l, f = to_table_data(data)
    chart_data = {
        "labels": l,
        "fields": f,
        "values": to_chart_data(table_data,l,f)
    }
    ret= {
        "chart": chart_data,
        "table": table_data
    }
    products = Product.get_all()
    return render(request, 'storage/order_analysis.html',
                  {
                      "products": products,
                      "data": ret
                  })


def enter_stat(request):
    return render(request,"storage/enter_stat.html")


def get_enter_datas(request):
    begin_data = request.GET.get("beginDate")  # 2018-05-01 00:00:00
    end_data = request.GET.get("endDate")  # 2018-05-01 23:59:59
    data = EnterStorage.get_stat_data(begin_data, end_data)
    return JsonResponse({"code": 200, "data": data})


def out_stat(request):
    return render(request, "storage/out_stat.html")


def get_out_datas(request):
    begin_data = request.GET.get("beginDate")  # 2018-05-01 00:00:00
    end_data = request.GET.get("endDate")  # 2018-05-01 23:59:59
    data = Order.get_stat_data(begin_data, end_data)
    print(data)
    return JsonResponse({"code": 200, "data": data})


def storage_list(request):
    rows = StorageInfo.get_info()
    return render(request, 'storage/storage_list.html', {"rows": rows})


def loss_list(request):
    products = Product.objects.all()
    return render(request, 'storage/loss_list.html',{'products': products})


def loss_add(request):
    id = request.POST.get("id")
    print(id)
    if id == '0':
        model = Loss()
    else:
        model = Loss.objects.get(id=id)
    model.product_id = request.POST.get('product')
    model.number = request.POST.get('number')
    model.desc = request.POST.get('desc')
    model.user = request.user
    model.state = 0
    model.save()
    return JsonResponse({"code": 200})


def get_loss_list(request):
    limit = int(request.GET.get("limit", 10))
    offset = int(request.GET.get("offset", 0))
    username = request.GET.get('user_name', "")
    state = request.GET.getlist('state')
    date_params = request.GET.get("create_at", "")
    query_params = {}
    if len(date_params) > 0:
        query_params["create_at__range"] = date_params.split(' ~ ')
    if len(username)>0:
        query_params["user__username"] = username
    if len(state) > 0:
        query_params["state__in"] = [int(s) for s in state]
    data = Loss.search(limit=limit, offset=offset, **query_params)
    return JsonResponse(data)


def get_loss(request):
    id = request.POST.get('id')
    model = Loss.objects.get(id=id)
    return JsonResponse({"code": 200, "data" : model.to_dict()})


def edit_loss(request):
    id = request.POST.get('code')
    state1 = request.POST.get('state')
    ids = id.split(',')
    if len(ids) > 1:
        for code in ids:
            model = Loss.objects.get(id=code)
            state = model.state
            model.state = state1
            update_storage(model, state)
        models = Loss.objects.filter(id__in=ids).update(state=state1, check_date=datetime.datetime.now(), check_user=request.user)
    else:
        model = Loss.objects.get(id=id)
        state = model.state
        model.check_date = datetime.datetime.now()
        model.state = state1
        model.check_desc = request.POST.get('check_desc')
        model.check_user = request.user
        model.save()
        update_storage(model, state)
    return JsonResponse({"code":200})


def update_storage(model,state):
    if model.state == '1':
        a = StorageInfo.objects.get(product_id=model.product.id)
        a.number = a.number - model.number
        a.save()
    if model.state == '2' and state == 1:
        a = StorageInfo.objects.get(product_id=model.product.id)
        a.number = a.number + model.number
        a.save()

    return JsonResponse({"code":200})


def exchange_list(request):
    return render(request, 'storage/exchange_list.html')