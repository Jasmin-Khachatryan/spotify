# Generated by Django 5.0.1 on 2024-01-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_artist",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_premium_user",
            field=models.BooleanField(default=False),
        ),
    ]
