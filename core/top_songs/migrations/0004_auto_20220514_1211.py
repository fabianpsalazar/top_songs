# Generated by Django 3.2.7 on 2022-05-14 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_songs', '0003_auto_20220513_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='artist_track',
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_track',
            field=models.ManyToManyField(to='top_songs.Track'),
        ),
    ]
