# Generated by Django 3.2.7 on 2022-05-13 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top_songs', '0002_auto_20220513_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='artist_trackId',
            new_name='artist_track',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='genre_trackId',
            new_name='genre_track',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='id',
            new_name='track',
        ),
    ]
