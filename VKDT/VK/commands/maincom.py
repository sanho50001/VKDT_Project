# import os
# import datetime
#
#
# class Maincom:
#
#     def __init__(self):
#         # Узнаем сегоднешнию дату
#         self.time_data = datetime.date.today()
#
#         # Узнаем в какой директории была запущенна программа
#         self.cur_dir = None
#
#         # Из директории обращаемся к папке с фото
#         self.from_file = None
#
#         # Достаем список всех файлов в папке
#         self.dir_file = os.listdir(self.from_file)
#
#         # Указываем папку выгрузки файлов
#         self.dir_files_downloading = None
#
#         # Указываем папку отгрузки файлов
#         self.dir_outdoing = None
#
#     def set_cur_dir(self, cur_dir):
#         self.cur_dir = cur_dir
#
#     def set_from_file(self, from_file):
#         self.from_file = from_file
#
#     def set_dir_file(self, dir_file):
#         self.dir_file = dir_file
#
#     def set_dir_files_downloading(self, dir_files_downloading):
#         self.dir_files_downloading = dir_files_downloading
#
#     def set_dir_outdoing(self, dir_outdoing):
#         self.dir_outdoing = dir_outdoing
#
#     def get_time_data(self):
#         return self.time_data
#
#     def get_cur_dir(self):
#         return self.cur_dir
#
#     def get_from_filea(self):
#         return self.from_file
#
#     def get_dir_file(self):
#         return self.dir_file
#
#     def get_dir_files_downloading(self):
#         return self.dir_files_downloading
#
#     def get_dir_outdoing(self):
#         return self.dir_outdoing
#
#     def set_cur_dir_from_file(self):
#         try:
#             # Из директории обращаемся к папке с фото
#             self.from_file = os.chdir('/home/app/web/media')
#
#             # Узнаем в какой директории была запущенна программа
#             self.cur_dir = str(os.getcwd())
#             self.dir_files_downloading = os.path.join(self.cur_dir, 'photo')
#             self.dir_outdoing = os.path.join(self.cur_dir, 'Outdoing', 'PhotoDay', str(self.time_data))
#         except FileNotFoundError as er:
#             os.makedirs('/home/app/web/media', exist_ok=True)
#             self.set_cur_dir_from_file()
