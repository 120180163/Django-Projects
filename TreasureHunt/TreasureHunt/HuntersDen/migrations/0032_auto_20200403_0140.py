# Generated by Django 3.0.1 on 2020-04-03 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HuntersDen', '0031_auto_20200403_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deninvitee',
            name='accepted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
