from django.db import models
from django.contrib.auth.models import User
from django.db import transaction,connection
from pystrich.ean13 import EAN13Encoder
from .sql import *
from meat.utils.mixin import DictMixin
from meat.settings import STORAGE_CONFIG


class Product(models.Model, DictMixin):
    """产品基础信息"""
    name = models.CharField(max_length=50)
    standard = models.CharField(max_length=20)
    packing = models.CharField(max_length=20)
    code = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    remark = models.CharField(max_length=50)
    state = models.IntegerField(default=1)

    class Meta:
        verbose_name = '产品'
        default_permissions = ()
        permissions = (
            ('product_list', '查看'),
            ('post_product', '编辑'),
            ('del_product', '删除'),
        )

    @classmethod
    def get(cls, id):
        try:
            return cls.objects.get(id=id)
        except:
            return None

    @classmethod
    def get_by_code(cls, code):
        try:
            return cls.objects.filter(code=code).first()
        except:
            return None

    @classmethod
    def get_stat_data(cls, begin, end):
        """获取入库统计数据"""
        cursor = connection.cursor()
        cursor.execute(stat_enter_sql.format(begin, end))
        result = cursor.fetchall()
        ret = []
        for item in result:
            ret.append({
                "name": item[0],
                "total_number": item[2],
                "total_price": item[3]
            })
        return ret

    @classmethod
    def get_all(cls):
        """查询全部"""
        rows = cls.objects.filter(state=1)
        return rows

    @classmethod
    def search(cls, **condation):
        q = models.Q(**{"state__gte": 0})
        total = cls.objects.count()
        rows = cls.objects.filter(q)
        return {
            "total": total,
            "rows": [m.to_dict() for m in rows],
        }

    @classmethod
    def del_product(cls, id):
        item = cls.objects.get(id=id)
        item.state = -1
        item.save()

    def create_barcode(self):
        """生产条形码"""
        code_name = "".join([STORAGE_CONFIG["BARCODE"]["ADDR"],
                             STORAGE_CONFIG["BARCODE"]["COM"],
                             self.code])
        encoder = EAN13Encoder(code_name)

        file_path = "".join([STORAGE_CONFIG["BARCODE"]["PATH"],
                             code_name, ".png"])
        encoder.save(file_path)
        return file_path

    def update(self, **kwargs):
        for k, v in kwargs.items():
            self[k] = v
        self.save(update_fields=[f for f in kwargs])

    @classmethod
    def search(cls, **kwargs):
        query = models.Q()
        for k, v in kwargs:
            if v is not None:
                q = models.Q(**{k:v})
                query.add(q)

        return cls.objects.filter(query)


class StorageInfo(models.Model, DictMixin):

    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    scattered_number = models.IntegerField(default=0)

    class Meta:
        verbose_name = '库存'
        default_permissions = ()
        permissions = (
            ("storage_list", "盘库"),
        )

    @classmethod
    def get_info(cls):
        """盘点库存信息"""
        rows = cls.objects.all()
        return rows

    @classmethod
    def update_storage(cls, product_id, number):
        model = cls.objects.filter(product_id=product_id).first()
        model.number += number
        model.save()

    def enter_storage(self, enter_model):
        with transaction.atomic():
            enter_model.save()
            self.update_storage(enter_model.product_id, enter_model.number)

    @classmethod
    def cancel_enter(cls, enter_id):
        model = EnterStorage.objects.get(id=enter_id)
        number = model.number
        product_id = - model.product.id
        with transaction.atomic():
            model.delete()
            s = cls.objects.filter(product_id=product_id).first()
            s.number += number
            s.save()


class EnterStorage(models.Model, DictMixin):
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    remark = models.CharField(max_length=50)

    class Meta:
        verbose_name = '入库'
        default_permissions = ()
        permissions = (
            ('storage_enter', '入库'),
            ('enter_stat', '入库统计'),
        )

    @classmethod
    def search(cls, limit=10, offset=0, condition={}):
        begin = limit*offset
        end = begin + limit
        data = cls.objects.all().order_by("-id")[begin:end]
        count = cls.objects.count()

        return {
            "total": count,
            "rows": [e.to_dict() for e in data]
        }

    @classmethod
    def get_stat_data(cls, begin, end):
        """获取出库统计数据"""
        cursor = connection.cursor()
        cursor.execute(stat_enter_sql.format(begin, end))
        result = cursor.fetchall()
        ret = []
        for item in result:
            ret.append({
                "name": item[0],
                "total_number": item[2],
                "total_price": item[3]
            })
        return ret


class Customer(models.Model, DictMixin):
    """出库收货单位"""
    customer_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        default_permissions = ()

    @classmethod
    def get(cls, pk):
        try:
            return cls.objects.get(pk)
        except:
            return None

    @classmethod
    def get_by_name(cls, name):
        return cls.objects.filter(customer_name=name).first()

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, keyword):
        ret = cls.objects.filter(customer_name__contains=keyword)
        return [c.to_dict() for c in ret]


class Order(models.Model, DictMixin):
    """出库订单"""
    create_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    hand_user = models.CharField(max_length=20, null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    money = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    remark = models.CharField(max_length=50)
    state = models.IntegerField(default=0)

    class Meta:
        verbose_name = '销售订单'
        default_permissions = ()
        permissions = (
            ('order', '查看订单'),
            ('order_edit', '创建订单'),
            ('delete_order', '删除订单'),
            ('out_stat', '销售统计'),
            ('order_analysis', '销售分析')
        )

    @classmethod
    def get(cls, pk):
        try:
            return cls.objects.get(id=pk)
        except Exception as e:
            return None

    @classmethod
    def get_stat_data(cls, begin, end):
        """获取出库统计数据"""
        cursor = connection.cursor()
        cursor.execute(stat_out_sql.format(begin, end))
        result = cursor.fetchall()
        ret = []
        for item in result:
            ret.append({
                "name": item[0],
                "total_number": item[1],
                "total_price": item[2]
            })
        return ret

    @classmethod
    def get_order_data(cls, id):
        """获取报表信息"""
        cursor = connection.cursor()
        cursor.execute(order_list_sql.format(id))
        result = cursor.fetchall()
        ret = []
        for item in result:
            ret.append({
                "code": item[0],
                "name": item[1],
                "number": item[2],
                "price": item[3],
                "money": item[4]
            })
        return ret

    @classmethod
    def search(cls, limit, offset, **condition):
        q = models.Q()
        for k, v in condition.items():
            q.add(models.Q(**{k: v}), models.Q.AND)
        total = cls.objects.filter(q).count()
        rows = cls.objects.filter(q)[offset:offset+limit]
        return {
            "total": total,
            "rows": [o.to_dict() for o in rows]
        }

    def create(self, detail):
        with transaction.atomic():
            self.save()
            if detail is not None:
                detail.order_id = self.id
                detail.save()

    @classmethod
    def remove_at(cls, pk):
        with transaction.atomic():
            OrderDetail.objects.filter(order_id=pk).delete()
            cls.objects.get(id=pk).delete()

    @classmethod
    def details(self, order_id):
        return OrderDetail.objects.filter(order_id=order_id)

    @classmethod
    def get_analysis_by_date(cls, begin_date, end_date, search_types):
        from django.db import connection
        from .const_sql import order_analysis_sql

        sql = order_analysis_sql.format(begin_date, end_date, ','.join(search_types))
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows


class OrderDetail(models.Model, DictMixin):
    """出库订单明细"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    remark = models.CharField(max_length=50)

    class Meta:
        default_permissions = ()

