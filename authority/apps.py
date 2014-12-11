import sys
from django.apps import AppConfig

class AuthorityConfig(AppConfig):
    name = "authority"

    def ready(self):

        import imp
        from django.conf import settings

        for app in settings.INSTALLED_APPS:
            try:
                __import__(app)
                app_path = sys.modules[app].__path__
            except AttributeError:
                continue
            try:
                imp.find_module('permissions', app_path)
            except ImportError:
                continue
            __import__("%s.permissions" % app)
            app_path = sys.modules["%s.permissions" % app]
