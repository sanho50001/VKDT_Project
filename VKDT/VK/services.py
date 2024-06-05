import os
import datetime
from dotenv import load_dotenv
import vk
import requests
from .models import VK
import os.path

load_dotenv()


class Maincom:

    def __init__(self):
        # Узнаем сегоднешнию дату
        self.time_data = datetime.date.today()

        # Узнаем в какой директории была запущенна программа
        self.cur_dir = None

        # Из директории обращаемся к папке с фото
        self.from_file = None

        # Достаем список всех файлов в папке
        self.dir_file = os.listdir(self.from_file)

        # Указываем папку выгрузки файлов
        self.dir_files_downloading = None

        # Указываем папку отгрузки файлов
        self.dir_outdoing = None

    def set_cur_dir(self, cur_dir):
        self.cur_dir = cur_dir

    def set_from_file(self, from_file):
        self.from_file = from_file

    def set_dir_file(self, dir_file):
        self.dir_file = dir_file

    def set_dir_files_downloading(self, dir_files_downloading):
        self.dir_files_downloading = dir_files_downloading

    def set_dir_outdoing(self, dir_outdoing):
        self.dir_outdoing = dir_outdoing

    def get_time_data(self):
        return self.time_data

    def get_cur_dir(self):
        return self.cur_dir

    def get_from_filea(self):
        return self.from_file

    def get_dir_file(self):
        return self.dir_file

    def get_dir_files_downloading(self):
        return self.dir_files_downloading

    def get_dir_outdoing(self):
        return self.dir_outdoing

    def set_cur_dir_from_file(self):
        try:
            # Из директории обращаемся к папке с фото
            self.from_file = os.chdir('/home/app/web/media')

            # Узнаем в какой директории была запущенна программа
            self.cur_dir = str(os.getcwd())
            self.dir_files_downloading = os.path.join(self.cur_dir, 'photo')
            self.dir_outdoing = os.path.join(self.cur_dir, 'Outdoing', 'PhotoDay', str(self.time_data))
        except FileNotFoundError as er:
            os.makedirs('/home/app/web/media', exist_ok=True)
            self.set_cur_dir_from_file()


class VKSaved:

    def __init__(self):
        self.requests = requests
        self.save_wall_photo = None
        self.photo_id = None
        self.photo_name = None
        self.saved = None

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

    def set_saved(self, saved):
        self.saved = saved

    def upload_in_vk(self, photo_name):

        # Задаём идентификатор группы, токен доступа, картинку и её описание
        group_id = os.getenv('group_id')
        access_token = os.getenv('access_token5')

        # Авторизуемся в VK
        session = vk.Session(access_token=access_token)
        vkapi = vk.API(session=session)
        upload_url = vkapi.photos.getWallUploadServer(group_id=group_id, v=5.131)['upload_url']
        requests = self.requests.post(upload_url, files={'file': open(photo_name, 'rb')})
        self.set_photo_name(photo_name)
        self.set_save_wall_photo(vkapi.photos.saveWallPhoto(group_id=group_id,
                                                            v=5.131,
                                                            photo=requests.json()['photo'],
                                                            server=requests.json()['server'],
                                                            hash=requests.json()['hash']))

        self.set_photo_id('photo' + str(self.get_save_wall_photo()[0]['owner_id']) + '_'
                          + str(self.get_save_wall_photo()[0]['id']))

        vkapi.wall.post(owner_id='-192102262', v=5.131, attachments=self.get_photo_id())
        vk_model_post = VK(text='',
                           post_id=self.get_photo_id(),
                           file_post=self.get_photo_name(),
                           post_image_url=f'')
        vk_model_post.save()
        return photo_name


class Queue:

    def __init__(self):
        self.start = None
        self.saved = None
        # self.queue_list = []
        self.last_photo = None
        self.last_time_photo_queue = None
        self.out_queue_list = []

    def set_start(self, start):
        self.start = start

    def set_saved(self, saved):
        self.saved = saved

    def set_last_time_photo_queue(self, time):
        self.last_time_photo_queue = time

    def set_last_photo(self, named_photo):
        self.last_photo = named_photo

    # def get_queue_list(self):
    #     return self.queue_list

    def get_last_time_photo_queue(self):
        return self.last_time_photo_queue

    def get_last_photo(self):
        return self.last_photo

    def mod_date(self, file):
        timed = os.path.getmtime(file)
        return datetime.datetime.fromtimestamp(timed)

    def out_queue(self):
        # Проходим по всей директории
        for file in self.start.get_dir_file():
            # находим файл который был изменен последним
            timed_file = self.mod_date(file)
            print(timed_file)
            # Если файл был по времени изменения меньше или равен времени последнего файла
            if timed_file <= self.get_last_time_photo_queue():
                self.set_last_time_photo_queue(time=timed_file)
                self.set_last_photo(named_photo=file)

            elif self.get_last_photo() == None:
                self.set_last_photo(named_photo=file)
                self.set_last_time_photo_queue(time=timed_file)


class VKontacte():

    def saved_in_vk(self):
        saved.upload_in_vk(photo_name=queue.get_last_photo())


# Инициализация команд
start = Maincom()
start.set_cur_dir_from_file()
saved = VKSaved()
queue = Queue()
vkontacte = VKontacte()

 # Настройка команд
queue.set_start(start=start)
queue.set_saved(saved=saved)
saved.set_saved(saved=saved)
