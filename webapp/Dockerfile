FROM python:3.7

RUN apt update &&\
    apt install -y supervisor nginx &&\
    pip3 install uwsgi

RUN useradd --no-create-home nginx
RUN rm /etc/nginx/sites-enabled/default

WORKDIR /opt/villager-or-not

COPY supervisord.conf /etc/supervisor/
COPY uwsgi.ini /etc/uwsgi/
COPY nginx.conf /etc/nginx/
COPY villager-or-not.conf /etc/nginx/conf.d/

COPY ./requirements.txt .
COPY ./export.pkl .
COPY ./templates ./app/templates

RUN pip3 install -r requirements.txt

COPY ./app/* /opt/villager-or-not/app/

CMD ["/usr/bin/supervisord"]
