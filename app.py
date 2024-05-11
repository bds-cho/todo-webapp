# Import dependencies
from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from datetime import datetime

# App and DB config
app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "password"
app.config['MYSQL_DB'] = "flaskDB"

# MySQL-DB connector
db = MySQL(app)

# Index
@app.route('/')
def index():
    dbexec = db.connection.cursor()
    dbexec.execute("SELECT * FROM todos")
    data = dbexec.fetchall()
    dbexec.close()
    return render_template('overview.html', todos=data)

# Overview
@app.route('/overview.html')
def overview():
    return redirect(url_for('index'))


# Edit
@app.route('/edit.html/<int:id_data>', methods=['GET', 'POST'])
def edit(id_data):
    #update task
    if request.method == 'POST':
        data = request.form    
        dbexec = db.connection.cursor()
        dbexec.execute("UPDATE todos SET des=%s, due=%s, comp=%s WHERE id=%s", (data['desc'],data['date'],data['comp'], id_data,))
        db.connection.commit()
        dbexec.close()
        return redirect(url_for('index'))    
    #retrieve data in edit.html
    else:  
        dbexec = db.connection.cursor()
        dbexec.execute("SELECT * FROM todos WHERE id=%s", (id_data,))
        task = dbexec.fetchone()
        dbexec.close()
        return render_template('edit.html', task=task)
   

# Delete
@app.route('/delete/<int:id_data>', methods =['GET'])
def delete(id_data):
    dbexec = db.connection.cursor()
    dbexec.execute("DELETE FROM todos WHERE id=%s", (id_data,))
    db.connection.commit()
    return redirect(url_for('index'))


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

    else:
        default_date = datetime.today().strftime('%Y-%m-%d')
        return render_template('create.html', default_date=default_date) 

    return render_template('create.html')


# Imprint
@app.route('/imprint.html')
def imprint():
    return render_template('imprint.html')


# Start
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # For development only
