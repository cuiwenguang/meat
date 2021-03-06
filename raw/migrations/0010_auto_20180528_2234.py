# Generated by Django 2.0.3 on 2018-05-28 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0009_auto_20180528_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collectdetail',
            options={'default_permissions': ()},
        ),
        migrations.AlterModelOptions(
            name='collectinfo',
            options={'default_permissions': (), 'permissions': (('collect_list', '查看'), ('collect_create', '称重'), ('collect_edit', '编辑'), ('collect_delete', '删除'), ('collect_payview', '结算'), ('collect_print', '删除'))},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': ()},
        ),
        migrations.AlterModelOptions(
            name='payinfo',
            options={'default_permissions': ()},
        ),
        migrations.AlterModelOptions(
            name='rawconfig',
            options={'default_permissions': (), 'permissions': (('config_edit', '配置编辑'),)},
        ),
        migrations.AlterModelOptions(
            name='sequence',
            options={'default_permissions': ()},
        ),
    ]
