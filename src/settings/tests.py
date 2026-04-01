import logging

from ._base import *

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']


class DisableMigrations:
    def __contains__(self, _):
        return True

    def __getitem__(self, _):
        return None


MIGRATION_MODULES = DisableMigrations()
logging.disable(logging.CRITICAL)
