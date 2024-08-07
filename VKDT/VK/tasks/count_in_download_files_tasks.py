import time
# from config.celery import app
import os

# @app.task
def count_in_download_files_task(task_id=1):

    while True:
        cur_dir = '/home/app/web/media'
        number = 0
        for root, dirs, files in os.walk(os.path.join(cur_dir, 'Outdoing', 'PhotoDay')):
            if len(files) > 0:
                number += len(files)
        return number

print(count_in_download_files_task())
