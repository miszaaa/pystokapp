from __future__ import absolute_import

import os
from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pystokapp.settings')

app = Celery('pystokapp')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# integration Celery with Django admin panel
app.conf.update(CELERY_RESULT_BACKEND='djcelery.backends.database.DatabaseBackend')
