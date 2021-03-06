# Generated by Django 3.0.5 on 2020-04-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('like', models.IntegerField(default=0)),
                ('haha', models.IntegerField(default=0)),
                ('sad', models.IntegerField(default=0)),
                ('angry', models.IntegerField(default=0)),
                ('numberOfDistribution', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
