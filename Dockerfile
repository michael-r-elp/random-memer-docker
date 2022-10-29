FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD app.py /
EXPOSE map[5000/tcp:{}]
CMD [ "python", "./app.py" ]
