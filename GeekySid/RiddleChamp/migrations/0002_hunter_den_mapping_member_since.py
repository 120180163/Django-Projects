# Generated by Django 3.0.1 on 2020-04-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiddleChamp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hunter_den_mapping',
            name='member_since',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
