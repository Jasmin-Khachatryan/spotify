# Generated by Django 4.2.9 on 2024-02-01 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_is_premium_user_user_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follows',
        ),
    ]