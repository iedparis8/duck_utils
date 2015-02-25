__author__ = 'paulguichon'
from django.conf import settings


def email_ied(individu):
    return str(individu.cod_etu) + '@foad.iedparis8.net'


def get_recipients(individu, cod_anu):
    if settings.DEBUG:
        recipients = (settings.EMAIL_DEV, )
    else:
        recipients = (individu.get_email(cod_anu), email_ied(individu))
    return recipients