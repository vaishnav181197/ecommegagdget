# Generated by Django 4.2.7 on 2023-11-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_product_exp_date_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(default='cart', max_length=100),
        ),
    ]
