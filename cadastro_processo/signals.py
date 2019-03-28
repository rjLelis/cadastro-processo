from django.db.models.signals import post_save
from processo.models import Processo
from django.dispatch import receiver
from .models import Planilha
import csv

@receiver(post_save, sender=Planilha)
def create_planilha(sender, instance, created, **kwargs):
    if created:
        with open(instance.arquivo.path) as arquivo:
            leitor = csv.reader(arquivo, delimiter=';')
            contador = 0
            for linha in leitor:
                if contador == 0:
                    contador += 1
                    continue
                processo = Processo(pasta=linha[0], comarca=linha[1], uf=linha[2], cliente=instance)
                processo.save()