# Based on ubuntu 22.04-lts
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt update -y && apt upgrade -y
RUN apt install -y python3 python3-pip python3-venv mysql-server libmysqlclient-dev pkg-config

# MySQL file and config
ADD ./init.sql /docker-entrypoint-initdb.d/
ENV MYSQL_ROOT_PASSWORD = password

# Add project files
ADD . /todo-website
WORKDIR /todo-website

# Prepare python environment
RUN python3 -m venv venv
RUN ./venv/bin/pip3 install --no-cache-dir flask flask-mysqldb

# Open port
EXPOSE 5000

# Add custom-entrypoint file
ADD ./custom-entrypoint.sh /usr/local/bin/

# Entrypoint
ENTRYPOINT ["custom-entrypoint.sh"]