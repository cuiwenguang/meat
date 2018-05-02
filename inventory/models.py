from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    standard = models.CharField(max_length=20)
    code = models.CharField(max_length=50)
    price = models.FloatField(default=0)


class StorageInfo(models.Model):
    pass


class PutInDetail(models.Model):
    pass

class PutOutDetail(models.Model):
    pass