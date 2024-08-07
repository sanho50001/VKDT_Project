import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Запуск для общего сервера
# app = Celery('config', backend='rpc://', broker='amqp://guest:guest@rabbit:5672')
# Запуск для локалки
app = Celery('VKDT')

# app = Celery('VKDT_project', backend='rpc://', broker='amqp://')
app.config_from_object("django.conf:settings", namespace="CELERY")
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
