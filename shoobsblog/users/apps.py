from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "shoobsblog.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import shoobsblog.users.signals  # noqa F401
        except ImportError:
            pass
