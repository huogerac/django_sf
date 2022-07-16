from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField


class Evento(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from='nome', overwrite=True, max_length=200, unique=True, db_index=True)
    imagem = models.URLField(max_length=1024, null=True, blank=True)
    site_link = models.URLField(max_length=1024, null=True, blank=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    def __str__(self):
        return str(self.user)


class Palestra(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='palestras')
    titulo = models.CharField(max_length=128)
    descricao = models.TextField()
    imagem = models.URLField(max_length=1024)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
