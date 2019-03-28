from django.apps import AppConfig


class CadastroProcessoConfig(AppConfig):
    name = 'cadastro_processo'

    def ready(self):
        import cadastro_processo.signal