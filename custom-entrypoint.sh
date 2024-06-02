#!/bin/bash
set -e

# Start MySQL server in the background
/etc/init.d/mysql start && service mysql status

# Wait for MySQL to fully start
until mysqladmin ping -h localhost --silent; do
  echo 'waiting for mysql to start...'
  sleep 2
done

# Execute the SQL initialization script
if [ -d "/docker-entrypoint-initdb.d" ]; then
  for file in /docker-entrypoint-initdb.d/*; do
    MYSQL_PWD=password mysql -u root < "$file"
  done
fi

# Start the Flask application
source ./venv/bin/activate
exec python3 app.py
