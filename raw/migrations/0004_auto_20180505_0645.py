# Generated by Django 2.0 on 2018-05-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0003_auto_20180505_0517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectinfo',
            old_name='cz_number',
            new_name='total_number',
        ),
        migrations.RenameField(
            model_name='collectinfo',
            old_name='cz_weight',
            new_name='total_price',
        ),
        migrations.AddField(
            model_name='collectinfo',
            name='total_weight',
            field=models.FloatField(default=0),
        ),
    ]
