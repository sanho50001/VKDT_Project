import requests
from bs4 import BeautifulSoup
import time
import urllib3


class Parsers:

    def __init__(self):
        self.number = 0

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number += number

    def parser_main_page(self, url='https://anime-pictures.net/posts?page=0&lang=ru'):
        """Парсер страницы anime-pictures"""
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        print('Начат процесс парсера | Запуск парсера по гл.странице')
        result = requests.get(url=url, verify=False)
        time.sleep(1)
        soup = BeautifulSoup(result.text, 'lxml')
        products = soup.find_all('div', class_='img-block svelte-1445hak img-block-big')
        for product in products:
            time.sleep(1)
            self.parser_main_page_info(product)

    def parser_main_page_info(self, product):
        """Парсер начальной страницы wowhead"""

        post_id = product.get('id')
        title_url = product.findNext().get('href')
        time.sleep(1)
        parse_data = self.parser_page(url='https://anime-pictures.net' + title_url)

        time.sleep(1)


        print('Конец парсера | Завершение')
        return

    def parser_page(self, url):
        """Парсер страницы"""

        p = requests.get(img)
        out = open(f"...\{self.get_number()}", "wb")
        self.set_number(1)
        out.write(p.content)
        out.close()

        return
