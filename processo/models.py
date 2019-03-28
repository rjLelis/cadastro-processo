from django.db import models

class Processo(models.Model):
    
    pasta = models.CharField(max_length=50)

    comarca = models.CharField(max_length=50)

    uf = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.pasta};{self.comarca};{self.uf}'