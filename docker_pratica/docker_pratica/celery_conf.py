from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
import logging

logger = logging.getLogger("Celery")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docker_pratica.settings')

app = Celery('docker_pratica')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
