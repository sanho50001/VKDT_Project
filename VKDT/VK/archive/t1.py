import os  # Узнаем в какой директории была запущенна программа
# # cur_dir = str(os.getcwd())
# # print(cur_dir)
#
# import requests
# from bs4 import BeautifulSoup
# import time
# import urllib3
#
# p = requests.get('https://i.pinimg.com/736x/11/98/d9/1198d9e9ddd67fd888d20eb21782d989.jpg')
# out = open(f"er.jpg", "wb")
#
# out.write(p.content)
# out.close()
#
#
# upper = [1,2,3,]
#
# upper.

# import zlib
#
# # compressed_data = 'https://oimages.anime-pictures.net/850/850773ddd286ff04cd9f4e562582cb58.png?if=ANIME-PICTURES.NET_-_829033-1890x2899-virtual+youtuber-nijisanji-kuzuha+%28nijisanji%29-hina+%28hinalovesugita%29-single-long+hair.png'  # Сжатые данные, полученные, например, из сети
# p = requests.get('https://oimages.anime-pictures.net/850/850773ddd286ff04cd9f4e562582cb58.png?if=ANIME-PICTURES.NET_-_829033-1890x2899-virtual+youtuber-nijisanji-kuzuha+%28nijisanji%29-hina+%28hinalovesugita%29-single-long+hair.png')
#
# with open(p.content, 'rb') as f:
#     data = bytearray(f.read())
#
# uncompressed_data = zlib.decompress(data, 16 + zlib.MAX_WBITS)
#
# with open('output.jpg', 'wb') as f:
#     f.write(uncompressed_data)

# import urllib
# urllib.urlretrieve('https://oimages.anime-pictures.net/d71/d71f3a6fec9663771a26a851461e97d1.png?if=ANIME-PICTURES.NET_-_828801-1500x1060-virtual+youtuber-nijisanji-yorumi+rena-hakase+fuyuki-kagami+hayato-kagami+hayato+%281st+costume%29.png',
#                    "...\img.jpg")

# import urllib2
#
# resource = urllib3.urlopen(img)
# out = open("...\img.jpg", 'wb')
# out.write(resource.read())
# out.close()


# import httplib2
#
# h = httplib2.Http('.cache')
# response, content = h.request('https://catherineasquithgallery.com/uploads/posts/2021-12/1639776871_337-catherineasquithgallery-com-p-kartinki-anime-na-fon-telefona-rozovie-452.jpg')
# out = open('img.jpg', 'wb')
# out.write(content)
# out.close()

os.chdir('/home/app/web/media')
# os.chdir('bootstrap-5.2.2-dist/bootstrap-5.2.2-dist/css')
print(os.chdir('bootstrap-5.2.2-dist/bootstrap-5.2.2-dist/css'))
print(str(os.getcwd()))