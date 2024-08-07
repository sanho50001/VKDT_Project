FROM python:3.10

WORKDIR /app

COPY ../../requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD ../../.. /app/
COPY ../../VK/photo /home/app/web/media
RUN rm /usr/local/lib/python3.10/site-packages/vk/utils.py
COPY docker_files/need/utils.py /usr/local/lib/python3.10/site-packages/vk/
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]