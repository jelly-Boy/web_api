# Generated by Django 3.0.2 on 2020-05-25 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApi', '0015_auto_20200525_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='music_service',
            field=models.ManyToManyField(related_name='ms_tracks', to='webApi.MusicService'),
        ),
        migrations.AlterField(
            model_name='track',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='g_tracks', to='webApi.Genre'),
        ),
    ]