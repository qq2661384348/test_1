from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.defaultfilters import date
from django.urls import reverse

from jinja2 import Environment


def environment(**options):
    """

    :param options:
    :return:
    """
    env = Environment(**options)
    env.globals.update({
        'date': date,
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env
