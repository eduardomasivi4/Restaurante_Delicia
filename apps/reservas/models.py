from django.db import models
from phonenumber_field.formfields import PhoneNumberField

class Reserva(models.Model):
    nome= models.CharField(max_length=150)
    telefone= PhoneNumberField(region='AO')
    email= models.EmailField()
    data = models.DateField()
    hora = models.TimeField()
    pessoas= models.IntegerField()
    observacoes= models.CharField(default='Nenhuma',null=False)