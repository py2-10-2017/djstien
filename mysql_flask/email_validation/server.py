from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')

app.secret_key = "923657325bfwyofbhkvbhbkhw8yt27o824bof"

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/add_email', methods=['POST'])
def useradd():
    session['email'] = request.form['email']
    email = session['email']
    errors = []
    if len(request.form['email']) < 1:
        errors.append('Email is not Valid')
        print errors
        flash("Email not valid")
        return redirect('/')
    else:
        get_emails = "SELECT * FROM emails"
        dbemails = mysql.query_db(get_emails,data=None)
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
             'email': request.form['email'], 
             'created_at': "NOW()",
             'updated_at': "NOW()"
           }
        print data 
        mysql.query_db(query, data)
        return render_template ('success.html', emails=dbemails)

app.run(debug=True)