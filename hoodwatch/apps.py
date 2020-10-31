from django.apps import AppConfig


class HoodwatchConfig(AppConfig):
    name = 'hoodwatch'

    def ready(self):
        import hoodwatch.signals
