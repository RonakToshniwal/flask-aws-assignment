
from datetime import datetime
import database
from crypt import methods
from flask import Flask,redirect, render_template, request,url_for

from bucket import addBucket,addEC2,getec2,deleteInstance,getBuckets,deleteBucket
app = Flask(__name__,template_folder='Template')
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/add")
def add():
    return render_template('add.html') 





@app.route("/show")
def show():
    rows=getBuckets()
    return render_template('show.html',rows=rows)  

@app.route("/delete/<id>")

def delete(id):
    deleteBucket(id)
    return redirect (url_for('show'))

@app.route("/addthis",methods=['POST','GET'])
def addthis():
    user=request.form
    addBucket(user['name'],user['location'])
    return redirect (url_for('home'))

@app.route("/addec2")
def addec2():
    return render_template ('addec2.html')

@app.route("/addthisec2",methods=['POST','GET'])
def addthisec2():
    print('added')
    addEC2()
    return redirect (url_for('home'))

@app.route("/showec2")
def showec2():
    rows=getec2()
    return render_template('showec2.html',rows=rows)  

@app.route("/delec2/<id>")

def delec2(id):
    print(id)

    deleteInstance(id)
    return redirect (url_for('showec2'))



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)