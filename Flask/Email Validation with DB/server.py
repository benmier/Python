from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector('mydb')
app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
	emails = mysql.fetch("SELECT * FROM users")
	return render_template('index.html', emails=emails)
@app.route('/email', methods=['POST'])
def create():
	if len(request.form['email'])<1:
		flash("No fields can be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	else: 
		flash("The email address you entered ({}) is a VALID email address! Thank you!".format(request.form['email']))
		query = "INSERT INTO users (id,email,created_at,updated_at) VALUES ('NULL', '{}', NOW(), NOW())".format(request.form['email'])
		mysql.run_mysql_query(query)
	return redirect('/')

@app.route('/delete', methods=['POST'])
def update():
	query = "DELETE FROM users WHERE id='{}'".format(request.form['delete'])
	mysql.run_mysql_query(query)
	return redirect('/')
app.run(debug=True)