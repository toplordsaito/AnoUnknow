# Generated by Django 3.0.3 on 2020-04-14 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0002_post_createby'),
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
                ('post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
