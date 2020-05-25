# Generated by Django 3.0.2 on 2020-05-24 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApi', '0008_genre_musicservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=30)),
                ('album', models.ForeignKey(default='No album', null=True, on_delete=django.db.models.deletion.SET_NULL, to='webApi.Album', to_field='album_name')),
                ('genre', models.ForeignKey(default='No genre', null=True, on_delete=django.db.models.deletion.SET_NULL, to='webApi.Genre', to_field='genre_name')),
                ('music_service', models.ManyToManyField(related_name='ms_tracks', to='webApi.MusicService')),
            ],
        ),
    ]