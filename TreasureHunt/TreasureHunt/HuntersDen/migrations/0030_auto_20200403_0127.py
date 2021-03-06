# Generated by Django 3.0.1 on 2020-04-03 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_userprofile_uin_code'),
        ('HuntersDen', '0029_responseimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='DenInvitee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_to', models.CharField(max_length=50)),
                ('invite_code', models.CharField(max_length=50)),
                ('sent_on', models.CharField(max_length=50)),
                ('accepted_on', models.CharField(max_length=50)),
                ('status', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='hunter_den_mapping',
            name='hunter_den',
        ),
        migrations.AddField(
            model_name='deninvitee',
            name='den',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HuntersDen.Den'),
        ),
        migrations.AddField(
            model_name='deninvitee',
            name='invitee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.UserProfile'),
        ),
    ]
