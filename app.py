# Import dependencies
from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL

# App and DB config
app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "flaskDB"

# MySQL-DB connector
db = MySQL(app)

# Index
@app.route('/')
def index():
    return render_template('overview.html')

# Overview
@app.route('/overview.html')
def overview():
    return redirect(url_for('index'))

# Edit
@app.route('/edit.html')
def edit():
    return render_template('edit.html')

# Create
@app.route('/create.html', methods=['GET','POST'])
def create(): 
    if request.method == 'POST':
        data = request.form
        dbexec = db.connection.cursor()
        dbexec.execute("INSERT INTO todos(des,due,comp) VALUES(%s,%s,%s)",(data['desc'],data['date'],data['comp']))
        db.connection.commit()
        dbexec.close()
        return redirect(url_for('index'))
    return render_template('create.html')

# Imprint
@app.route('/imprint.html')
def imprint():
    return render_template('imprint.html')

# Start
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # For development only
