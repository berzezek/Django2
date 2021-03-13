from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # 1.6

    def ready(self): # подгружаем когда приложение готово
        import users.signals # Могут быть неправильно импортирваны... нужно через UsersConfig(AppConfig)... или __init__ 1.7
