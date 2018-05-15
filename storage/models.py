from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from pystrich.ean13 import EAN13Encoder

from meat.utils.mixin import DictMixin
from meat.settings import STORAGE_CONFIG

class Product(models.Model, DictMixin):
    """产品基础信息"""
    name = models.CharField(max_length=50)
    standard = models.CharField(max_length=20)
    packing = models.CharField(max_length=20)
    code = models.CharField(max_length=50, db_index=True)
    price = models.FloatField(default=0)
    remark = models.CharField(max_length=50)
    state = models.IntegerField(default=1)

    @classmethod
    def get(cls, id):
        try:
            return cls.objects.get(id=id)
        except:
            return None

    @classmethod
    def get_all(cls):
        """查询全部"""
        q = models.Q(**{"state__gte": 0})
        # total = cls.objects.count()
        rows = cls.objects.filter(q)
        return [m.to_dict() for m in rows]

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


class StorageInfo(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    scattered_number = models.IntegerField(default=0)

    @classmethod
    def update_storage(cls, product_id, number):
        model = cls.objects.filter(product_id=product_id).first()
        model.number += number
        model.save()

    def enter_storage(self, enter_model):
        with transaction.atomic():
            enter_model.save()
            self.update_storage(enter_model.product_id, enter_model.number)


class EnterStorage(models.Model):
    create_at = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    remark = models.CharField(max_length=50)



class OutStorage(models.Model):
    crate_at = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    remark = models.CharField(max_length=50)
