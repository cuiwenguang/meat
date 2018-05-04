import datetime
from django.contrib.auth.models import User
from django.db import models


class TransDict:
    """queryset转字典"""
    def to_dict(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, attr), TransDict):
                d[attr] = getattr(self, attr).to_dict()
            elif isinstance(getattr(self, attr), User):
                d[attr] = getattr(self,attr).username
            else:
                d[attr] = getattr(self, attr)
        return d


class RawConfig(models.Model, TransDict):
    """系统参数配置表"""
    default_number = models.IntegerField(default=5)  #默认每次可称重数量
    default_tare = models.FloatField(default=0)  # 默认皮重
    unit_of_weight = models.CharField(max_length=10, default="KG")  # 重量计量单位
    unit_of_number = models.CharField(max_length=10, default="只(头)")  # 数量计量单位

    class Meta:
        permissions =(
            ("view_config", "允许查看"),
            ("manage_config", "允许管理（CRUD）"),
        )


class Customer(models.Model, TransDict):
    id_card = models.CharField(max_length=20)
    cust_name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)

    class Meta:
        permissions =(
            ("view_customer", "允许查看"),
            ("manage_customer", "允许管理（CRUD）"),
        )

class Category(models.Model, TransDict):
    """原料基础信息"""
    name = models.CharField(max_length=50)
    default_price = models.FloatField(default=0)
    type = models.CharField(max_length=50, null=True, blank=True)
    state = models.IntegerField(default=1)


class CollectInfo(models.Model, TransDict):
    """收购信息"""
    sg_no = models.CharField(max_length=50)  # 收购批次
    sg_datetime = models.DateTimeField(auto_now=True)  # 收购时间
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)  # 客户账号
    cz_weight = models.FloatField(default=0)  # 收购称重重量
    cz_number = models.IntegerField(default=0)  # 收购数量
    sg_source = models.CharField(max_length=100, default='')  # 收购来源
    state = models.IntegerField(default=1)  # 数据状态，备用
    user = models.ForeignKey(User, related_name='collect_user', null=True, on_delete=models.SET_NULL)  # 收购操作员



class CollectDetail(models.Model, TransDict):
    """收购明细"""
    collect_info = models.ForeignKey(CollectInfo, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.IntegerField()
    weight = models.FloatField()
    price = models.FloatField()


class PayInfo(models.Model, TransDict):
    collect_info = models.ForeignKey(CollectInfo, on_delete=models.CASCADE)
    pay_money = models.FloatField(default=0)
    create_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='pay_user', null=True, on_delete=models.SET_NULL)  # 结算操作员




