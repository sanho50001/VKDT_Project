import time
# from celery import shared_task
from config.celery import app
from VK.services import start_download_file


@app.task
def download_task(task_id=1):

    while True:
        print('Старт загрузки файлов')
        start_download_file()
        print('')
        print('Загрузка файлов завершенна.')
