from django.db import models

class MenuItem(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data = models.DateField()
    hora = models.TimeField()
    pessoas = models.IntegerField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} - {self.data}"