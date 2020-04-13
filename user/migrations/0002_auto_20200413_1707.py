# Generated by Django 3.0.3 on 2020-04-13 17:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Authen_User',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('normal_user', models.BooleanField(default=True)),
                ('ban_user', models.BooleanField(default=datetime.datetime(2020, 4, 13, 17, 7, 46, 129863))),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BanUserModel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ban_date', models.DateField(null=True)),
                ('remark', models.TextField(null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='RandomUserModel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
