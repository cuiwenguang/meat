# Generated by Django 2.0.5 on 2018-06-02 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0011_auto_20180602_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'default_permissions': (), 'permissions': (('order', '查看订单'), ('order_edit', '创建订单'), ('delete_order', '删除订单'), ('out_stat', '销售统计'), ('order_analysis', '销售分析')), 'verbose_name': '销售订单'},
        ),
    ]
