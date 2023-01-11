# Generated by Django 3.2.12 on 2022-03-08 10:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=16383, null=True)),
                ('query', models.TextField()),
                ('date_of_query', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.IntegerField(null=True)),
                ('image', models.ImageField(default='us_ma.png', upload_to='post_images/')),
                ('cv', models.FileField(blank=True, null=True, upload_to='post_files/')),
                ('cgpa', models.FloatField(default=0.0, null=True)),
                ('complete_address', models.CharField(max_length=16383, null=True)),
                ('gender', models.CharField(max_length=16383, null=True)),
                ('profile_filled', models.BooleanField(default=False)),
                ('profile_created', models.DateTimeField(default=datetime.datetime(2022, 3, 8, 16, 17, 47, 685782))),
                ('account_banned_permanent', models.BooleanField(default=False)),
                ('account_banned_temporary', models.BooleanField(default=False)),
                ('account_ban_date', models.DateTimeField(blank=True, null=True)),
                ('account_ban_time', models.IntegerField(default=0)),
                ('signup_date', models.DateTimeField(default=datetime.datetime(2022, 3, 8, 16, 17, 47, 685782))),
                ('verified', models.BooleanField(default=False)),
                ('otp_time', models.DateTimeField(default=datetime.datetime(2022, 3, 8, 16, 17, 47, 685782))),
                ('otp', models.CharField(max_length=16383, null=True)),
                ('got_internship', models.BooleanField(default=False)),
                ('unique_code', models.CharField(max_length=16383, null=True)),
                ('unique_code_time', models.DateTimeField(default=datetime.datetime(2022, 3, 8, 16, 17, 47, 685782))),
                ('code_expired', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.IntegerField(null=True)),
                ('complete_address', models.CharField(max_length=16383, null=True)),
                ('image', models.ImageField(default='us_ma.png', upload_to='post_images/')),
                ('profile_filled', models.BooleanField(default=False)),
                ('profile_created', models.DateTimeField(default=datetime.datetime(2022, 3, 8, 16, 17, 47, 687796))),
                ('account_banned_permanent', models.BooleanField(default=False)),
                ('account_banned_temporary', models.BooleanField(default=False)),
                ('account_ban_date', models.DateTimeField(blank=True, null=True)),
                ('account_ban_time', models.IntegerField(default=0)),
                ('signup_date', models.DateTimeField(default=datetime.datetime(2022, 3, 8, 16, 17, 47, 688050))),
                ('verified', models.BooleanField(default=False)),
                ('otp_time', models.DateTimeField(default=datetime.datetime(2022, 3, 8, 16, 17, 47, 688050))),
                ('otp', models.CharField(max_length=16383, null=True)),
                ('unique_code', models.CharField(max_length=16383, null=True)),
                ('unique_code_time', models.DateTimeField(default=datetime.datetime(2022, 3, 8, 16, 17, 47, 688050))),
                ('code_expired', models.BooleanField(default=False)),
                ('let_staff_manage', models.BooleanField(default=False)),
                ('engaged', models.BooleanField(default=False)),
                ('is_this_staff_superuser', models.BooleanField(default=False)),
                ('staff_last_name', models.CharField(max_length=16383, null=True)),
                ('staff_first_name', models.CharField(max_length=16383, null=True)),
                ('original_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ORIGINAL', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MAIN_USER', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ORDINARY_USER', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]