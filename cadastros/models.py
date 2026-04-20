from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    estado = models.CharField(max_length=2, verbose_name="UF", help_text="Ex: PR, SP, RJ")

    def __str__(self):
        return f"{self.nome} ({self.estado})"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ["nome"]
