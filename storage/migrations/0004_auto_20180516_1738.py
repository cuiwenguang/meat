# Generated by Django 2.0 on 2018-05-16 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_auto_20180511_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterstorage',
            old_name='Product',
            new_name='product',
        ),
    ]
