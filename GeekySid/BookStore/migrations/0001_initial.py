# Generated by Django 3.0.1 on 2020-04-08 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=300)),
                ('landmark', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=6)),
                ('message', models.CharField(max_length=200)),
                ('paymode', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=2500)),
                ('category', models.CharField(default='', max_length=20)),
                ('date_add', models.DateField()),
                ('price', models.FloatField()),
                ('discount', models.FloatField(default=0.0)),
                ('image', models.ImageField(default='', upload_to='image/shop/')),
            ],
        ),
        migrations.CreateModel(
            name='Ordered_Product',
            fields=[
                ('order_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('discount', models.FloatField()),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=300)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_desc', models.TextField()),
                ('remark', models.TextField(default='We will contact you via mail')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Order')),
            ],
        ),
    ]
