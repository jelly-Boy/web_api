# Generated by Django 3.0.2 on 2020-05-25 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApi', '0016_auto_20200525_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='music_service',
            field=models.ManyToManyField(null=True, related_name='ms_tracks', to='webApi.MusicService'),
        ),
    ]
