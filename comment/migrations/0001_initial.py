# Generated by Django 3.0.3 on 2020-04-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('like', models.IntegerField(default=0)),
                ('haha', models.IntegerField(default=0)),
                ('sad', models.IntegerField(default=0)),
                ('angry', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
