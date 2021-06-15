FROM python:3.9.2

MAINTAINER Edward jimenez "edward.jimenez@blackboard.com"

RUN apt-get update || : && apt-get install python -y
RUN apt-get install -y python-dev

RUN mkdir /app
WORKDIR /app
COPY .. .
RUN pip install --upgrade pip
RUN pip install -r pip-requirements.txt
RUN python /app/app/config/keys/build_config.py
ENV PYTHONPATH "${PYTHONPATH}:./app"
EXPOSE 5000

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "wsgi:application"]
