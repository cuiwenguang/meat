from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """产品基础信息"""
    name = models.CharField(max_length=50)
    standard = models.CharField(max_length=20)
    packing = models.CharField(max_length=20)
    code = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    remark = models.CharField(max_length=50)
    state = models.IntegerField(default=1)


class StorageInfo(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    scattered_number = models.IntegerField(default=0)


class EnterStorage(models.Model):
    crate_at = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    remark = models.IntegerField(max_length=50)


class OutStorage(models.Model):
    crate_at = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0)
    remark = models.CharField(max_length=50)
