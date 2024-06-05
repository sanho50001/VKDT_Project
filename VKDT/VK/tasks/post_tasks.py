import time
# from celery import shared_task
from config.celery import app
from VK.services import *


@app.task
def post_task(task_id=1):

    while True:
        print('Начат процесс таска | Post')
        print('Начат процесс таска | Find file')
        queue.out_queue()
        print('Завершение | Find file')
        print()
        print('Отправка в VK | Post')
        file = vkontacte.saved_in_vk()
        print('Пост выложен | Post')
        print()

        vkontacte.replaced(file=file)
        print('Отправка в сон | Post')
        minutes = 30
        secundes = 60
        time.sleep(minutes * secundes)
        print('Возвращение из сна. | Post')
