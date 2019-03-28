from django.db import models
from cadastro_processo.models import Planilha

class Processo(models.Model):
    
    pasta = models.CharField(max_length=50)

    comarca = models.CharField(max_length=50)

    uf = models.CharField(max_length=2)

    cliente = models.ForeignKey(Planilha, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.pasta};{self.comarca};{self.uf}'