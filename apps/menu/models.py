from django.db import models

class Pratos(models.Model):
    Tipo_de_prato = [
        ("ENTRADAS/STARTERS","ENTRADAS/STARTERS"),
        ("MASSA E OVOS/PASTA & EGGS", "MASSA E OVOS/PASTA & EGGS"),
        ("SALADAS/SALADS", "SALADAS/SALADS"),
        ("ESPECIALIDADES DO CHEFE/CHEF'S SPECIALITIES", "ESPECIALIDADES DO CHEFE/CHEF'S SPECIALITIES"),
        ("SOBREMESAS/DESSERTS", "SOBREMESAS/DESSERTS"),
    ]

    imagem = models.ImageField(upload_to='imagem/pratos', null=True)
    nome = models.CharField(max_length= 100)
    foreign_lang_nome = models.CharField(max_length= 100)
    descricao = models.TextField(default='Sem descrição')
    foreign_lang_descricao = models.TextField(default='No description')
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    tipo_de_prato= models.CharField(max_length=50, choices=Tipo_de_prato)
