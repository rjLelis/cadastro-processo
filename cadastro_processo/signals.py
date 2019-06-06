from django.db.models.signals import post_save
from processo.models import Processo
from django.dispatch import receiver
from .models import Planilha
import csv

@receiver(post_save, sender=Planilha)
def create_planilha(sender, instance, created, **kwargs):
    if created:
        with open(instance.arquivo.path) as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=';')
            for linha in leitor:
                pasta, comarca, uf = linha.values()
                processo = Processo(pasta=pasta, comarca=comarca, uf=uf, cliente=instance)
                processo.save()