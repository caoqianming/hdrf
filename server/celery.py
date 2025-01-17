import os
from . import conf
from celery import Celery
from celery.app.control import Control, Inspect

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery(conf.BASE_PROJECT_CODE)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

celery_control: Control = Control(app=app)
celery_inspect: Inspect = celery_control.inspect()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
