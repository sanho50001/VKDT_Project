# from dotenv import load_dotenv
# import os
# import vk
# import requests
# from VK.models import VK
# load_dotenv()
#
#
# class VKSaved:
#     def __init__(self):
#         self.requests = requests
#         self.save_wall_photo = None
#         self.photo_id = None
#         self.photo_name = None
#         self.saved = None
#
#     def set_save_wall_photo(self, exp):
#         self.save_wall_photo = exp
#
#     def get_save_wall_photo(self):
#         return self.save_wall_photo
#
#     def set_photo_id(self, exp):
#         self.photo_id = exp
#
#     def get_photo_id(self):
#         return self.photo_id
#
#     def set_photo_name(self, exp):
#         self.photo_name = exp
#
#     def get_photo_name(self):
#         return self.photo_name
#
#     def set_saved(self, saved):
#         self.saved = saved
#
#     def saved(self, photo_name):
#
#         # Задаём идентификатор группы, токен доступа, картинку и её описание
#         group_id = os.getenv('group_id')
#         access_token = os.getenv('access_token5')
#
#         # Авторизуемся в VK
#         session = vk.Session(access_token=access_token)
#
#         vkapi = vk.API(session=session)
#
#         upload_url = vkapi.photos.getWallUploadServer(group_id=group_id, v=5.131)['upload_url']\
#
#         requests = self.requests.post(upload_url, files={'file': open(photo_name, 'rb')})
#
#         self.set_photo_name(photo_name)
#
#         self.set_save_wall_photo(vkapi.photos.saveWallPhoto(group_id=group_id,
#                                                             v=5.131,
#                                                             photo=requests.json()['photo'],
#                                                             server=requests.json()['server'],
#                                                             hash=requests.json()['hash']))
#
#         self.set_photo_id('photo' + str(self.get_save_wall_photo()[0]['owner_id']) + '_'
#                           + str(self.get_save_wall_photo()[0]['id']))
#
#         vkapi.wall.post(owner_id='-192102262', v=5.131, attachments=self.get_photo_id())
#         vk_model_post = VK(text='',
#                            post_id=self.saved.get_photo_id(),
#                            file_post=self.saved.get_photo_name(),
#                            post_image_url=f'')
#         vk_model_post.save()
#         return photo_name