# Generated by Django 2.0 on 2018-05-05 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectdetail',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='raw.Category'),
        ),
        migrations.AddField(
            model_name='collectdetail',
            name='m_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='collectdetail',
            name='p_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='collectdetail',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='collectdetail',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='collectdetail',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
