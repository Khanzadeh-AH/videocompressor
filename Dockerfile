FROM python:3.9.13-slim-buster
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade -r /code/requirements.txt
COPY ./ /code
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]