# Generated by Django 2.2.3 on 2019-10-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20191016_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='dispatch_qty',
            field=models.CharField(default='', max_length=100),
        ),
    ]
