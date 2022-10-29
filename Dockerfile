FROM python:3.8-slim-buster
EXPOSE 80/tcp
ADD Docker/ /
ADD app.py /
RUN apt-get clean \
    && apt-get -y update
RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential
RUN pip install -r requirements.txt
COPY Docker/nginx.conf /etc/nginx
RUN chmod +x ./start.sh
CMD ["./start.sh"]