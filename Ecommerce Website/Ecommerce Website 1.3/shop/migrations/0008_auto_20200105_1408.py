# Generated by Django 3.0.1 on 2020-01-05 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order_status_ordered_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_status',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='ordered_product',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='ordered_product',
            old_name='product_id',
            new_name='product',
        ),
    ]
