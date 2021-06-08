FROM node:16.2.0

MAINTAINER Edward jimenez "edward.jimenez@blackboard.com"

RUN mkdir /app

COPY docker/startServices.sh /app/.
RUN chmod 777 /app/startServices.sh

RUN apt-get update || : && apt-get install python3 -y
RUN apt-get install python3-pip -y python3-dev

RUN mkdir /app/backend
WORKDIR /app/backend
COPY .. .
RUN pip3 install --upgrade pip
RUN pip3 install -r pip-requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/app/backend/app"

RUN mkdir /app/frontend
WORKDIR /app/frontend
RUN git clone https://github.com/blackboard/BBDN-LTI-Tool-Provider-React .
RUN npm install
#RUN npm build
#RUN mv docker/nginx.conf /etc/nginx/conf.d/default.conf
#EXPOSE 3000


WORKDIR /app
ENTRYPOINT ["./startServices.sh"]

