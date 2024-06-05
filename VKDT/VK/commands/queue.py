# import datetime
# import os.path
#
#
# class Queue:
#
#     def __init__(self):
#         self.start = None
#         self.saved = None
#         # self.queue_list = []
#         self.last_photo = None
#         self.last_time_photo_queue = None
#         self.out_queue_list = []
#
#     def set_start(self, start):
#         self.start = start
#
#     def set_saved(self, saved):
#         self.saved = saved
#
#     def set_last_time_photo_queue(self, time):
#         self.last_time_photo_queue = time
#
#     def set_last_photo(self, named_photo):
#         self.last_photo = named_photo
#
#     # def get_queue_list(self):
#     #     return self.queue_list
#
#     def get_last_time_photo_queue(self):
#         return self.last_time_photo_queue
#
#     def get_last_photo(self):
#         return self.last_photo
#     #
#     # def queue(self):
#     #     # Достаем все файлы и добавляем в очередь
#     #     self.queue_list.append(self.start.get_dir_file())
#
#     def mod_date(self, file):
#         timed = os.path.getmtime(file)
#         return datetime.datetime.fromtimestamp(timed)
#
#     def out_queue(self):
#         # Проходим по всей директории
#         for file in self.start.get_dir_file():
#             # находим файл который был изменен последним
#             timed_file = self.mod_date(file)
#             print(timed_file)
#             # Если файл был по времени изменения меньше или равен времени последнего файла
#             if timed_file <= self.get_last_time_photo_queue():
#                 self.set_last_time_photo_queue(time=timed_file)
#                 self.set_last_photo(named_photo=file)
#
#             elif self.get_last_photo() == None:
#                 self.set_last_photo(named_photo=file)
#                 self.set_last_time_photo_queue(time=timed_file)
#
