FROM python:3.8-slim-buster
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD app.py /
EXPOSE 5000/tcp
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
