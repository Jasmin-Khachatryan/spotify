# Generated by Django 5.0.1 on 2024-01-21 13:46

import helpers.upload_image
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("artist", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="artist",
            name="cover_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=helpers.upload_image.upload_artist_image,
            ),
        ),
        migrations.AddField(
            model_name="artist",
            name="pseudonym",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
