# Generated by Django 5.0.1 on 2024-01-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="music",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="music/"),
        ),
    ]
