# Generated by Django 3.0.1 on 2019-12-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='date_add',
            field=models.DateField(),
        ),
    ]