__author__ = 'nervosa'
from django.conf import settings

def add_settings_to_context(request):
    all_settings = {}
    all_settings['DEBUG'] = settings.DEBUG
    all_settings['INSTALLED_APPS'] = settings.INSTALLED_APPS
    all_settings['LANGUAGE_CODE'] = settings.LANGUAGE_CODE
    all_settings['ADMINS'] = settings.ADMINS

    # if necessary implement passing other settings

    return all_settings