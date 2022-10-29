FROM python:3.8-slim-buster
EXPOSE 5000/tcp
ADD Docker/ /
RUN pip install -r requirements.txt
ADD app.py /
RUN apt-get -y install nginx
COPY nginx.conf /etc/nginx
RUN chmod +x ./start.sh
CMD ["./start.sh"]