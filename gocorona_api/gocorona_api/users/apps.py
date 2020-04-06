from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "gocorona_api.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import gocorona_api.users.signals  # noqa F401
        except ImportError:
            pass
