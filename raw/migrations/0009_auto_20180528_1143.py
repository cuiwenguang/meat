# Generated by Django 2.0 on 2018-05-28 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0008_delete_permission'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'default_permissions': (), 'permissions': (('view_category', '查看'), ('edit_category', '编辑'), ('delete_category', '删除'))},
        ),
        migrations.AlterModelOptions(
            name='rawconfig',
            options={'default_permissions': (), 'permissions': (('view_rawconfig', '允许查看'),)},
        ),
    ]
