# Generated by Django 3.0.8 on 2023-01-11 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 0, 56, 27, 646018)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 0, 56, 27, 645993)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 0, 56, 27, 646011)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='unique_code_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 0, 56, 27, 646026)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 0, 56, 27, 645716)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 0, 56, 27, 645685)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 0, 56, 27, 645709)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='unique_code_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 0, 56, 27, 645729)),
        ),
    ]
