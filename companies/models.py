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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Employee(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="employees",
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        Company,
        related_name="employees",
        on_delete=models.CASCADE,
    )
