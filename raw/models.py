import datetime
from django.contrib.auth.models import User
from django.db import models
from meat.utils.mixin import DictMixin


class RawConfig(models.Model, DictMixin):
    """系统参数配置表"""
    default_number = models.IntegerField(default=5)  # 默认每次可称重数量
    default_tare = models.FloatField(default=0)  # 默认皮重
    unit_of_weight = models.CharField(max_length=10, default="KG")  # 重量计量单位
    unit_of_number = models.CharField(max_length=10, default="只(头)")  # 数量计量单位

    class Meta:
        verbose_name = '参数配置模块'
        default_permissions = ()
        permissions = (
            ("config_edit", "配置编辑"),
        )


class Customer(models.Model, DictMixin):
    id_card = models.CharField(max_length=20)
    cust_name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)

    class Meta:
        default_permissions = ()

    @classmethod
    def save_and_get(cls, id_card, **kwargs):
        try:
            c = cls.objects.get(id_card=id_card)
        except:
            c = Customer(id_card=id_card)
        c.cust_name = kwargs["cust_name"]
        c.address = kwargs["address"]
        c.mobile = kwargs["mobile"]
        c.save()
        return c


class Category(models.Model, DictMixin):
    """原料基础信息"""
    name = models.CharField(max_length=50)
    default_price = models.FloatField(default=0)
    type = models.CharField(max_length=50, null=True, blank=True)
    state = models.IntegerField(default=1)

    class Meta:
        verbose_name = '品种分类'
        default_permissions = ()
        permissions = (
            ("category_list", "查看"),
            ("post_category", "编辑"),
            ("delete_category", "删除"),
        )

    @classmethod
    def get_categories(cls):
        return cls.objects.filter(state__gt=0)


class CollectInfo(models.Model, DictMixin):
    """收购信息"""
    state_choice = (
        (0, "暂存"),
        (1, "未结算"),
        (2, "结算中"),
        (3, "完成"),
    )
    sg_no = models.CharField(max_length=50, db_index=True)  # 收购批次
    sg_datetime = models.DateTimeField(auto_now=True)  # 收购时间
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)  # 客户账号
    total_price = models.FloatField(default=0)
    total_number = models.IntegerField(default=0)
    total_weight = models.FloatField(default=0)
    sg_source = models.CharField(max_length=100, default='')  # 收购来源
    state = models.IntegerField(default=0)  # 数据状态，备用
    user = models.ForeignKey(User, related_name='collect_user', null=True, on_delete=models.SET_NULL)  # 收购操作员

    class Meta:
        verbose_name = "收购"
        default_permissions = ()
        permissions = (
            ('collect_list', '查看'),
            ('collect_create', '称重'),
            ('collect_edit', '编辑'),
            ('collect_delete', '删除'),
            ('collect_payview', '结算'),
            ('collect_print', '打印'),
        )

    def update_total_fields(self):
        total = CollectDetail.objects \
            .filter(collect_info_id=self.id) \
            .values('collect_info_id') \
            .annotate(total_price=models.Sum(models.F('price') * models.F('weight')),
                      total_number=models.Sum('number'),
                      total_weight=models.Sum('weight'))[0]
        self.total_price = total["total_price"]
        self.total_number = total['total_number']
        self.total_weight = total['total_weight']
        self.save()

    @classmethod
    def search(cls, offset, limit, **kwargs):
        q = models.Q()
        for k, v in kwargs.items():
            c = {}
            if k == "sg_date" and len(v) == 2:
                c["sg_datetime__range"] = v
            elif k == "sg_state" and len(v) > 0:
                c["state__in"] = v
            elif k == "customer" and len(v) > 0:
                c["customer__cust_name"] = v
            elif k == 'no':
                if len(v) > 0:
                    c['sg_no'] = v
            q.add(models.Q(**c), q.AND)
        count = cls.objects.filter(q).count()
        ret = cls.objects.filter(q)[offset:offset + limit]
        return {
            "total": count,
            "rows": [c.to_dict() for c in ret]
        }


class CollectDetail(models.Model, DictMixin):
    """收购明细"""
    collect_info = models.ForeignKey(CollectInfo, db_index=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, db_index=True, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    p_weight = models.FloatField(default=0)
    m_weight = models.FloatField(default=0)
    price = models.FloatField(default=0)
    seq = models.IntegerField(default=1)

    class Meta:
        default_permissions = ()


class PayInfo(models.Model, DictMixin):
    collect_info = models.ForeignKey(CollectInfo, db_index=True, on_delete=models.CASCADE)
    pay_money = models.FloatField(default=0)
    create_at = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, related_name='pay_user', null=True, on_delete=models.SET_NULL)  # 结算操作员

    class Meta:
        default_permissions = ()

    @classmethod
    def get_pay_sum(cls, id):
        ret = PayInfo.objects.filter(collect_info_id=id).values('collect_info_id').annotate(
            sum_price=models.Sum('pay_money'))
        if len(ret) == 0:
            return 0
        return ret[0]["sum_price"]


class Sequence(models.Model):
    """自增序列"""
    key_name = models.CharField(max_length=2, db_index=True)
    number = models.IntegerField(default=0)

    class Meta:
        default_permissions = ()

    @staticmethod
    def get(key):
        try:
            seq = Sequence.objects.get(key_name=key)
        except:
            seq = Sequence(key_name=key, number=0)
        seq.number = seq.number + 1
        seq.save()
        return seq.number


def get_sg_no():
    """获取一个收购编号"""
    pre = datetime.datetime.now().strftime("%y%m%d")
    seq = Sequence.get(pre)
    s = "".join(['0'] * (4 - len(str(seq))))
    return "".join((pre, s, str(seq)))
