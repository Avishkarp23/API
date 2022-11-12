import mysql.connector
from flask import Flask,jsonify,request

import json
app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/loginget/<name>')
def fetch_data(name):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gdsc")
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("select password from login_details where email ='"+ str(name)+"'")
    result = mycursor.fetchall()
    return jsonify(result)

@app.route('/loginpost',methods=["POST"])
def post_data():
    data=request.form
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gdsc")
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(f"insert into login_details values('{data['email']}','{data['password']}')")
    return jsonify(data)



    
    
if __name__=="__main__":
    app.run(debug=True,port=8000)







