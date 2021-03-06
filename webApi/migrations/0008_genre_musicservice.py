# Generated by Django 3.0.2 on 2020-05-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApi', '0007_auto_20200525_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MusicService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_service_name', models.CharField(max_length=40, unique=True)),
                ('url', models.URLField(unique=True)),
            ],
        ),
    ]
