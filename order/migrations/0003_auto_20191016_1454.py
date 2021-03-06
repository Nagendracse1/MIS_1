# Generated by Django 2.2.3 on 2019-10-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20191013_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='dispatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatch_qty', models.CharField(blank=True, default='', max_length=100)),
                ('dispatch_date', models.CharField(blank=True, default='', max_length=100)),
                ('total_supplied_qty', models.CharField(blank=True, default='', max_length=100)),
                ('balance_qty', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='balance_qty',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='dispatch_date',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='dispatch_qty',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='total_supplied_qty',
        ),
    ]
