from django.db import models


class GenderChoice(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "female"
