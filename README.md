# Programmierpraktikum Skalierbare Systeme HA12-10
### Deployment steps on Ubuntu:
1. Install packages: `apt install -y python3 python3-pip python3-venv mysql-server libmysqlclient-dev pkg-config`
2. Make sure mysql-server is running: `/etc/init.d/mysql start && service mysql status`
3. Create DB and table using MySQL's command-line client:
    - `CREATE DATABASE flaskDB;`
    - `USE flaskDB;`
    - `CREATE TABLE todos(id INT AUTO_INCREMENT PRIMARY KEY, des VARCHAR(100), due DATE, comp INT);`
4. Clone this repo: `git clone https://git.tu-berlin.de/bschouhan_29/pp-sksy-ha12-10.git`
5. Switch directory to cloned repo: `cd pp-sksy-ha12-10`
6. Create python venv: `python3 -m venv ./venv`
7. Activate venv: `source ./venv/bin/activate`
8. Install python dependencies: `pip install flask flask-mysqldb`
9. Start flask server: `python3 app.py`
10. Test on your browser: `http://localhost:5000`