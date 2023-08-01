FROM python:3.10

WORKDIR /usr/src/bot/

COPY  . /usr/src/bot/

RUN pip install --user -U --pre aiogram
RUN pip install --user environs

CMD ["python", "main.py"]