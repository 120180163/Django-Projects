# Generated by Django 3.0.1 on 2020-04-02 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HuntersDen', '0028_auto_20200401_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='image/response/')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HuntersDen.Response')),
            ],
        ),
    ]
