FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY . .

RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py loaddata start_data.json
