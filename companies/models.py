from django.db import models
from django.conf import settings


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="companies",
        on_delete=models.CASCADE,
    )
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="company",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name
