FROM python:3.10

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app/

CMD ["python", "VKDT\VK\VK_main.py"]