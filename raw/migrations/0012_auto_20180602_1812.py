# Generated by Django 2.0.5 on 2018-06-02 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0011_auto_20180528_2242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'default_permissions': (), 'permissions': (('category_list', '查看'), ('post_category', '编辑'), ('delete_category', '删除')), 'verbose_name': '品种分类'},
        ),
        migrations.AlterModelOptions(
            name='collectinfo',
            options={'default_permissions': (), 'permissions': (('collect_list', '查看'), ('collect_create', '称重'), ('collect_edit', '编辑'), ('collect_delete', '删除'), ('collect_payview', '结算'), ('collect_print', '打印'), ('stat_list', '统计')), 'verbose_name': '收购'},
        ),
    ]
