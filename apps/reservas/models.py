from django.db import models
class Reserva(models.Model):
    nome= models.CharField(max_length=150)
    telefone= models.CharField(default=None,max_length=9)
    email= models.EmailField()
    data = models.DateField()
    hora = models.TimeField()
    pessoas= models.IntegerField()
    observacoes= models.CharField(default='Nenhuma',null=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome