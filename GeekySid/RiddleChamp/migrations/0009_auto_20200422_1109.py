# Generated by Django 3.0.1 on 2020-04-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiddleChamp', '0008_riddle_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riddle',
            name='audio',
            field=models.FileField(blank=True, upload_to='audio/riddle/'),
        ),
    ]