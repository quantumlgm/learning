FROM ubuntu:25.10
LABEL author=Ruslan
RUN apt-get update
RUN apt-get install apache2 -y
WORKDIR /var/www/html/
COPY ./index.html .
ENV OWNER=ADMIN
ENV PASS=secretkey111
EXPOSE 80
CMD [ "apache2ctl", "-D", "FOREGROUND" ]

