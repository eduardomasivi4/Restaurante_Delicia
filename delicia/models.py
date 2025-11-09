from django.db import models

class Pratos(models.Model):
    nome = models.CharField (max_length= 200)
    descricao = models.TextField (default= 'Sem descrição')
    preco = models.DecimalField (max_digits= 8, decimal_places= 2, default= 0.00)

    def __str__(self):
        return self.nome

class Bebidas (models.Model):
    nome= models.CharField (max_length= 150)
    descricao = models.TextField (default= 'Sem descrição')
    preco = models.DecimalField (max_digits= 8, decimal_places= 2, default= 0.00)
    preco_por_taca= models.BooleanField('Preço por taça/copo', default=False)
    
    def __str__(self):
        return self.nome

class Reservar(models.Model):
    nome_completo= models.CharField (max_length= 250)
    email= models.EmailField()
    telefone= models.IntegerField()
    data= models.DateField()
    hora= models.TimeField()
    num_de_pessoas= models.IntegerField('Nº de pessoas')
    observacoes= models.TextField()

    def __str__(self):
        return self.nome_completo
