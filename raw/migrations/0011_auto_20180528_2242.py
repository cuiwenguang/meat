# Generated by Django 2.0.3 on 2018-05-28 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0010_auto_20180528_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'default_permissions': (), 'permissions': (('view_category', '查看'), ('edit_category', '编辑'), ('delete_category', '删除')), 'verbose_name': '品种分类'},
        ),
        migrations.AlterModelOptions(
            name='collectinfo',
            options={'default_permissions': (), 'permissions': (('collect_list', '查看'), ('collect_create', '称重'), ('collect_edit', '编辑'), ('collect_delete', '删除'), ('collect_payview', '结算'), ('collect_print', '删除')), 'verbose_name': '收购'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'default_permissions': ()},
        ),
        migrations.AlterModelOptions(
            name='rawconfig',
            options={'default_permissions': (), 'permissions': (('config_edit', '配置编辑'),), 'verbose_name': '参数配置模块'},
        ),
    ]
