# Generated by Django 4.2.9 on 2024-01-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("artist", "0005_artist_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
    ]
