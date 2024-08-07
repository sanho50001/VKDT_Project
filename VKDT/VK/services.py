import json
import os
import datetime
import random
import time
from dotenv import load_dotenv
import vk
import requests
import shutil
# from .models import VK
import os.path

load_dotenv()


class VKAPI:
    """Класс работы с API ВК."""

    def __init__(self):

        access_token = os.getenv('access_token5')

        self.requests = requests    # библиотека запросов
        self.save_wall_photo = None     #
        self.photo_id = None    # Айди фото
        self.photo_name = None  # Имя файла
        self.session = vk.Session(access_token=access_token)
        self.vkapi = vk.API(session=self.session, v=5.131)

    def set_save_wall_photo(self, exp):
        self.save_wall_photo = exp

    def get_save_wall_photo(self):
        return self.save_wall_photo

    def set_photo_id(self, exp):
        self.photo_id = exp

    def get_photo_id(self):
        return self.photo_id

    def set_photo_name(self, exp):
        self.photo_name = exp

    def get_photo_name(self):
        return self.photo_name

    def set_session(self, session):
        self.session = session

    def set_vkapi(self, vkapi):
        self.vkapi = vkapi

    def upload_in_vk(self, photo_name):
        # Задаём идентификатор группы, токен доступа, картинку и её описание

        group_id = os.getenv('group_id')
        # Авторизуемся в VK

        upload_url = self.vkapi.photos.getWallUploadServer(group_id=group_id, v=5.131)['upload_url']
        requests = self.requests.post(upload_url, files={'file': open(photo_name, 'rb')})
        self.set_photo_name(photo_name)
        self.set_save_wall_photo(self.vkapi.photos.saveWallPhoto(group_id=group_id,
                                                                 v=5.131,
                                                                 photo=requests.json()['photo'],
                                                                 server=requests.json()['server'],
                                                                 hash=requests.json()['hash']))

        self.set_photo_id('photo' + str(self.get_save_wall_photo()[0]['owner_id']) + '_'
                          + str(self.get_save_wall_photo()[0]['id']))

        post = self.vkapi.wall.post(owner_id='-192102262', v=5.131, message='#art', attachments=self.get_photo_id())

        # vk_model_post = VK(text='art',
        #                    post_id=f'https://vk.com/wall-192102262_{post.get('post_id')}',
        #                    file_post=self.get_photo_name(),
        #                    post_image_url=f'')
        # vk_model_post.save()
        print('Пост выложен | Post VK')
        return photo_name

    def json_dump(self, id_group):
        """Функция отправляет запрос на получение API VK"""
        data = self.vkapi.wall.get(owner_id=f'-{id_group}', offset=2, count=100)
        with open(f'{os.path.join(logic.get_cur_dir(),"JSON_data", f"data-{id_group}.json") }', 'w',
                  encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def json_load(self, id_group):
        """Функция считывает полученный JSON"""
        with open(f'{os.path.join(logic.get_cur_dir(),"JSON_data", f"data-{id_group}.json") }', 'r',
                  encoding='utf-8') as file:
            data = json.load(file)
        return data

    def data_load(self, data, id_group):
        """Функция проходит по JSON'у и считывает все URL."""
        number = 0
        for attach in data['items']:
            for photo in attach['attachments']:
                try:
                    for val, key in photo['photo']['orig_photo'].items():
                        if val == 'url':
                            self.download_data(key=key, number=number, id_group=id_group)
                            number += 1
                            time.sleep(random.randint(10, 15))
                except KeyError as err:
                    print(f'error {err}')
        return number

    def download_data(self, key, number, id_group):
        """Функция скачивания файлов по URL"""
        response = requests.get(key, stream=True)

        with open(f'{os.path.join(logic.get_dir_catalog_downloading(), f"{id_group} {number} img.jpg")}', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return

    def main_download_files(self):
        """Функция загрузки файлов."""
        art_number = 0
        try:
            for id_group in os.getenv('id_groups').split(','):
                self.json_dump(id_group=id_group)
                data = self.json_load(id_group=id_group)
                number = self.data_load(data=data, id_group=id_group)
                art_number += number
                print(
                    f'Загрузка файлов из группы "{id_group}" завершенно. Было скаченно: {number} файлов. Всего: {art_number}')
        except (Exception, TypeError) as err:
                print(
                    f'Загруженно файлов было всего: {art_number}')
                print(err)


class Logic:
    """Главный класс с функционалом """
    def __init__(self):
        # Узнаем сегоднешнию дату
        self.time_data = datetime.date.today()

        # Узнаем в какой директории была запущенна программа
        self.cur_dir = None

        # Из директории обращаемся к папке с фото
        self.dir_catalog_downloading = None

        # Достаем список всех файлов в папке
        self.dir_file = None

        # Указываем папку отгрузки файлов
        self.dir_outdoing = None

    def set_cur_dir(self, cur_dir):
        """Установка в какой директории была запущенна программа"""
        self.cur_dir = cur_dir

    def set_dir_catalog_downloading(self, dir_catalog_downloading):
        """Установка директории куда будут скачиваться все файлы и откуда будут браться файлы для загрузки на стену"""
        self.dir_catalog_downloading = dir_catalog_downloading

    def set_dir_file(self, dir_file):
        """Установка директории для чтения файлов"""
        self.dir_file = dir_file

    def set_dir_outdoing(self, dir_outdoing):
        """Установка директории куда будут переноситься файлы и сортироваться по времени загрузки на стену"""
        self.dir_outdoing = dir_outdoing

    def get_time_data(self):
        """Установка времени"""
        return self.time_data

    def get_cur_dir(self):
        """Функция возвращает переменную cur_dir (в какой директории запущенна программа)"""
        return self.cur_dir

    def get_dir_catalog_downloading(self):
        """Функция возвращает переменную dir_catalog_downloading (директория загрузки фотографий)"""
        return self.dir_catalog_downloading

    def get_dir_file(self):
        """Функция возвращает переменную dir_file (директория из которой считываются файлы)"""
        return self.dir_file

    def get_dir_outdoing(self):
        """Функция возвращает переменную dir_outdoing (директория складирования/выгрузки фотографий)"""
        return self.dir_outdoing

    def set_cur_dir_from_file(self):
        """Функция возвращает переменную cur_dir_from_file (в какой директории запущенна программа)
        Так же устанавливает все переменные

        """
        try:

            # if not os.path.exists('/home/app/web/media'):
            #     os.makedirs('/home/app/web/media', exist_ok=True)
            # Из директории обращаемся к папке с фото
            # vps
            # self.dir_catalog_downloading = os.chdir('/home/app/web/media')

            # local
            self.set_cur_dir(os.getcwd())  # Узнаем текущий каталог

            self.set_dir_catalog_downloading(
                os.path.join(self.get_cur_dir(), 'photo'))  # Устанавливаем папку откуда будем брать картинки
            # main
            self.set_dir_file(os.path.join(self.get_cur_dir()))  # Установка каталога

            self.set_dir_outdoing(
                os.path.join(
                    self.get_cur_dir(),
                    'Outdoing',
                    'PhotoDay',
                    str(self.time_data)
                ))

            # Если каталога нет,то создается каталог, иначе просто перемещается
            if not os.path.exists(self.get_dir_outdoing()):
                os.makedirs(self.get_dir_outdoing())
            if not os.path.exists(self.get_dir_catalog_downloading()):
                os.makedirs(self.dir_catalog_downloading())
            if not os.path.exists(os.path.join(self.get_cur_dir(), 'JSON_data')):
                os.makedirs(os.path.join(self.get_cur_dir(), 'JSON_data'))
        except FileNotFoundError as er:
            os.makedirs('/home/app/web/media', exist_ok=True)
            self.set_cur_dir_from_file()


class Queue:
    """Класс псевдо очереди"""
    def __init__(self):
        self.logic = None   # Логика
        self.vkapi = None   # Апи ВК
        self.last_photo = None  # Последнее фото (необходимо для работы и проверки)
        self.last_time_photo_queue = None   #Время последнего фото в очереди
        self.out_queue_list = []    #Очередь (возможно удалю)

    def set_logic(self, logic):
        """Передача класса Логики для дальнейшей работы"""
        self.logic = logic

    def set_vkapi(self, vkapi):
        """Передача класса АПИ ВК для дальнейшей работы"""
        self.vkapi = vkapi

    def set_last_time_photo_queue(self, time):
        """Установка время последнего файла"""
        self.last_time_photo_queue = time

    def set_last_photo(self, named_photo):
        """Установка последнего файла для проверки и отправки"""
        self.last_photo = named_photo

    def get_last_time_photo_queue(self):
        """Взятие последнего файла для проверки и отправки в очередь (возможно удалю)"""
        return self.last_time_photo_queue

    def get_last_photo(self):
        """Получение последнего фото"""
        return self.last_photo

    def mod_date(self, file):
        """Проверка файла по времени для дальнейшей логики (чем старее тем ближе к отправке)"""
        timed = os.path.getmtime(file)
        return datetime.datetime.fromtimestamp(timed)

    def find_file_to_send(self):
        """Фукнция подготовки файла к отправке"""
        # Проходим по всей директории
        catalog = self.logic.get_dir_catalog_downloading()    # Установка каталога по которому будет итерация
        for file in os.listdir(catalog):
            # находим файл который был изменен последним
            timed_file = self.mod_date(os.path.join(catalog, file))

            # Если файл был по времени изменения меньше или равен времени последнего файла
            # Если последнего файла не было
            if self.get_last_photo() == None:
                self.set_last_time_photo_queue(time=timed_file)
                self.set_last_photo(named_photo=file)
                return
            elif timed_file <= self.get_last_time_photo_queue():
                self.set_last_photo(named_photo=file)
                self.set_last_time_photo_queue(time=timed_file)
                return
        time.sleep(2)
        return

    def replace_last_file(self):
        """Функция перемещения последнего файла"""

        # Если каталога нет,то создается каталог, иначе просто перемещается
        if not os.path.exists(self.logic.get_dir_outdoing()):
            os.makedirs(self.logic.get_dir_outdoing())

        file = shutil.move(
            os.path.join(self.logic.get_dir_catalog_downloading(), self.get_last_photo()),  # То откуда перенести
            os.path.join(self.logic.get_dir_outdoing(), self.get_last_photo())  # куда перести
        )
        return


def start_upload_file(minutes, secundes):
    """Функция старта отправки файлов """
    while True:

        try:
            queue.find_file_to_send()
            vkapi.upload_in_vk(photo_name=os.path.join(logic.get_dir_catalog_downloading(), queue.get_last_photo()))
            queue.replace_last_file()

        except (Exception, TypeError) as err:
            print(err)
        time.sleep(minutes * secundes)
        print('Отправка в сон | Post VK')

def start_download_file():
    """Функция старта загрузки файлов"""
    try:
        vkapi.main_download_files()
    except (Exception, TypeError) as err:
        print(err)


# Инициализация команд
logic = Logic()
logic.set_cur_dir_from_file()
vkapi = VKAPI()
queue = Queue()

 # Настройка команд
queue.set_logic(logic=logic)
queue.set_vkapi(vkapi=vkapi)


if __name__ == '__main__':
    try:
        logic.set_cur_dir_from_file()
        start_upload_file()
        # start_download_file()
    except (Exception, TypeError) as err:
        print(err)

