# Generated by Django 5.0.1 on 2024-01-24 04:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0009_album_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
