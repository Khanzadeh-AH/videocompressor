FROM python:3.9.13-slim-buster
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade -r /code/requirements.txt
COPY ./ /code
ENV DB_NAME='compress'
ENV DB_USER='postgre'
ENV DB_PASSWORD='postgre'
ENV DB_HOST='127.0.0.1'
ENV DB_PORT='5432'
ENV REDIS_HOST='127.0.0.1'
ENV REDIS_PORT='6379'

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]