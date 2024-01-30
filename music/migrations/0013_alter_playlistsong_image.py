# Generated by Django 4.2.9 on 2024-01-26 14:44

from django.db import migrations, models
import helpers.upload_image


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0012_remove_music_category_music_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playlistsong",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=helpers.upload_image.upload_playlist_image,
            ),
        ),
    ]