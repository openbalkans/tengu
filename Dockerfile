FROM python:3.7.4-stretch

RUN mkdir -p /var/tengu
COPY . /var/tengu

RUN pip install /var/tengu

ENV SQLALCHEMY_DATABASE_URI sqlite://

CMD tengu -p 5000 --init-db
