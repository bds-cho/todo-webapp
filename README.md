# Programmierpraktikum Skalierbare Systeme HA12-10
### Deployment steps on Ubuntu:
1. Install packages: `apt install -y python3 python3-pip python3-venv mysql-server`
2. Create DB and table using MySQL's commad-line client: [createDB.txt](./createDB.txt)
3. Clone this repo: `git clone https://git.tu-berlin.de/bschouhan_29/pp-sksy-ha12-10.git`
4. Switch directory to cloned repo: `cd pp-sksy-ha12-10`
5. Create python venv: `python -m venv ./venv`
6. Activate venv: `source ./venv/bin/activate`
7. Install python dependencies: `pip install flask flask-mysqldb`
8. Start flask server: `python app.py`
9. Test on your browser: `http://localhost:5000`