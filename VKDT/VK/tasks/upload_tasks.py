import time
# from celery import shared_task
from config.celery import app
from VK.services import *


@app.task
def upload_task(task_id=1):

    while True:
        print('Начат процесс таска | Post VK')
        print()
        print('Отправка в VK | Post VK')
        minutes, secundes = 30, 60
        start_upload_file(minutes=minutes, secundes=secundes)
        print()
        print('Возвращение из сна. | Post VK')

