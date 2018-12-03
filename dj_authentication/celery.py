from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apps.app_authenciate.settings')
# app = Celery('apps.app_authenciate')
# app.config_from_object('django.conf:settings', namespace='app_authenciate')
# app.autodiscover_tasks()

os.environ.setdefault('DJANGO_SETTINGS_MODULE','dj_authentication.settings')
# app = Celery('dj_authentication')
app = Celery('dj_authentication',broker='redis://127.0.0.1:6379/2')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


