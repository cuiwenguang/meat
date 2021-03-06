# Generated by Django 2.0.3 on 2018-06-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0012_auto_20180602_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
    ]
