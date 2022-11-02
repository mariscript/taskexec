from django.db import models
from django.conf import settings

# from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name

# class ThemeConfiguration(models.Model):
#     THEME = [
#         (True, _('dark')),
#         (False, _('light')),
#     ]
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE)
#     theme = models.BooleanField(_('theme'), default=True)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['user'],
#             name='One Entry Per User',)
#         ]

# class Theme(models.Model):
#     color = models.CharField(max_length=1000)
#     user = models.CharField(max_length=1000)

#     def __str__(self):
#         return self.user
