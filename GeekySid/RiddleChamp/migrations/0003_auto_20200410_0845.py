# Generated by Django 3.0.1 on 2020-04-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiddleChamp', '0002_hunter_den_mapping_member_since'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hunter_den_mapping',
            name='member_since',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
