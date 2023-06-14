from flask import Flask,render_template,redirect
from pymongo import MongoClient
import os


app = Flask(__name__)

def get_db():
    client = MongoClient('mongodb+srv://gof:fusxsh28ApW8USpq@cluster0.elawff4.mongodb.net/')
    
    db = client['GOF-DB-new']
    return db

@app.route('/')
def appfnc():
    db = get_db()
    teslcol = db['test']
    teslcol.insert_one({
        'name':"aon",
        'age':'28',
        'sex':'male'
    })
    
    return 'hii'

@app.route('/home')
def homefnc():
    data = [1,2,3,4,5,6]
    return render_template('home.html',data = data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')