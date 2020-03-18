from django.apps import AppConfig

class BashmycodeConfig(AppConfig):
    name = 'bashmycode'

    def ready(self):
        import signals