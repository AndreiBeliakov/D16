from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portal_news'
    # нам надо переопределить метод ready, чтобы при готовности
    # нашего приложения импортировался модуль со всеми функциями обработчиками

    def ready(self):
        import portal_news.signals