from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
mysql = MySQLConnector(app,'login_auth')
bcrypt = Bcrypt(app)
app.secret_key = "bfhew869efyob2eoyybo3byf4fl4f"


@app.route('/')
def index():
    query1 = "SELECT * FROM users"
    query_results = mysql.query_db(query1)
    print query_results
    return render_template ('index.html', users=query_results)

@app.route('/login', methods=['POST'])
def success_log():

    query2 = "SELECT pw_hash, id FROM users WHERE email = :email"
    data = {
        "email": request.form["email"]
    }
    query2_results = mysql.query_db(query2, data)
    print query2_results
    

    if not query2_results: 
        return render_template ('register.html')
    else:
        return render_template ('success.html')

@app.route('/register', methods=['POST'])
def register_user():
    hashed_pw = bcrypt.generate_password_hash(request.form["password"])
    query3 = "INSERT INTO users (email, pw_hash, first_name, last_name) VALUES (:email, :password, :fname, :lname)"
    data = {
        "email": request.form['email'],
        "password": hashed_pw,
        "fname": request.form["fname"],
        "lname": request.form["lname"]
    }
    query3_results = mysql.query_db(query3,data)
    print query3_results
    return render_template ("success.html")

app.run(debug=True)