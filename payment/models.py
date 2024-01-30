from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.IntegerField()
    stripe_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.name}"
