from django.db import models

class Planilha(models.Model):

    nome = models.CharField(max_length=100)
    
    cliente = models.CharField(max_length=100)
    
    arquivo = models.FileField(upload_to='files/')


    def __repr__(self):
        return self.nome