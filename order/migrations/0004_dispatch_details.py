# Generated by Django 2.2.3 on 2019-10-16 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20191016_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatch',
            name='details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispatch', to='order.OrderDetails'),
        ),
    ]
