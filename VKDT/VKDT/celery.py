import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlizNews.settings')

# Запуск для общего сервера
# app = Celery('BlizNews', backend='rpc://', broker='amqp://guest:guest@rabbit:5672')
# Запуск для локалки
app = Celery('VKDT_project')

# app = Celery('BlizNews', backend='rpc://', broker='amqp://')
app.config_from_object("django.conf:settings", namespace="CELERY")
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
