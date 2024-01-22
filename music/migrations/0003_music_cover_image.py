# Generated by Django 5.0.1 on 2024-01-21 13:36

import helpers.upload_image
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0002_music_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="music",
            name="cover_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=helpers.upload_image.upload_music_cover_image,
            ),
        ),
    ]
