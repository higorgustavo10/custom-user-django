from django.db import models


class Material(models.Model):
    titulo = models.CharField(max_length=150)
    descicao = models.TextField()

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'

    def __str__(self):
        return self.titulo





