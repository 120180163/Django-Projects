# Generated by Django 3.0.1 on 2020-04-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HuntersDen', '0027_auto_20200331_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='denriddle',
            name='uin_code',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='den',
            name='riddle_start_time',
            field=models.TimeField(blank=True),
        ),
    ]
