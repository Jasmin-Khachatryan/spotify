# Generated by Django 5.0.1 on 2024-01-21 14:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0004_music_artist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="music",
            name="artist",
        ),
    ]
