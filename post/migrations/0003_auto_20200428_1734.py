# Generated by Django 3.0.3 on 2020-04-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200425_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='numberOfDistribution',
            field=models.IntegerField(default=20),
        ),
    ]
