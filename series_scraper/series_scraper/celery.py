import os
from celery import Celery
from django.conf import settings
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'series_scraper.settings')
app = Celery('series_scraper')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-every-5-seconds': {
        'task': 'update_db',
        'schedule': 5.0,
        'args': (16, 16)
    },
}

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))