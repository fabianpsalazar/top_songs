# Generated by Django 4.0.4 on 2022-05-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artistId',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genreId',
            field=models.CharField(max_length=100),
        ),
    ]
