from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    sobre = models.TextField()
    imagem = models.URLField(max_length=1024, null=True, blank=True)
    github_link = models.URLField(max_length=1024, null=True, blank=True)
    twitter_link = models.URLField(max_length=1024, null=True, blank=True)
    site_link = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return str(self.user)
