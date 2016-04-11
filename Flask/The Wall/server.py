from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'\d')
PASS_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$')
app = Flask(__name__)
mysql = MySQLConnector('friendsdb2')
app.secret_key = "ThisIsSecret!"
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
	if len(request.form['email'])<2 or len(request.form['first_name'])<2 or len(request.form['last_name'])<2:
		flash("All fields must contain at least 2 characters")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address")
	elif len(request.form['password'])<8:
		flash("Password must contain at least 8 characters")
	elif NAME_REGEX.search(request.form['first_name']) or NAME_REGEX.search(request.form['last_name']):
		flash("Name fields cannot contain numbers")
	elif str(request.form['password']) != str(request.form['confirm']):
		flash("Passwords do not match!")
	elif not PASS_REGEX.match(request.form['password']):
		flash("Password must contain at least 1 uppercase letter and 1 number")
	else: 
		flash("Thank you {}, your account has been created for {}".format(request.form['first_name'],request.form['email']))
		pw_hash = bcrypt.generate_password_hash(request.form['password'])
		query = "INSERT INTO users (id,first_name,last_name,email,password,created_at,updated_at) VALUES ('NULL','{}','{}','{}','{}',NOW(),NOW())".format(request.form['first_name'],request.form['last_name'],request.form['email'],pw_hash)
		mysql.run_mysql_query(query)
	return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	loggedIn = mysql.fetch("SELECT * FROM users JOIN messages ON users.id = messages.user_id WHERE email='{}' ORDER BY messages.created_at desc".format(request.form['email']))
	session['loggedIn'] = loggedIn
	test = bcrypt.check_password_hash(loggedIn[len(loggedIn)-1]['password'], request.form['password'])
	if loggedIn == []:
		flash("Unknown Email")
		return redirect('/')
	elif not bcrypt.check_password_hash(loggedIn[len(loggedIn)-1]['password'], request.form['password']):
		flash("Incorrect password")
		return redirect('/')
	return redirect('/wall')

@app.route('/wall')
def wall():
	session['loggedIn'] = mysql.fetch("SELECT message,first_name,last_name,messages.id AS messages_id,users.id,users.email,messages.created_at FROM users JOIN messages ON users.id = messages.user_id WHERE email='{}' ORDER BY messages.created_at desc".format(session['loggedIn'][len(session['loggedIn'])-1]['email']))
	session['commentQuery'] = mysql.fetch("SELECT first_name,last_name,comments.created_at,comment,users.id AS user_id,comments.id AS comment_id,messages.id AS messages_id FROM users JOIN messages ON users.id = messages.user_id JOIN comments ON messages.id = comments.message_id WHERE email='{}' GROUP BY comment_id".format(session['loggedIn'][len(session['loggedIn'])-1]['email']))
	return render_template('wall.html', loggedIn=session['loggedIn'], commentQuery=session['commentQuery'])

@app.route('/postMessage', methods=['POST'])
def postMessage():
	query = "INSERT INTO messages (id,message,created_at,updated_at,user_id) VALUES ('NULL','{}',NOW(),NOW(),'{}')".format(request.form['messageText'],session['loggedIn'][len(session['loggedIn'])-1]['user_id'])
	mysql.run_mysql_query(query)
	return redirect('/wall')

@app.route('/postComment', methods=['POST'])
def postComment():
	query = "INSERT INTO comments (id,comment,created_at,updated_at,user_id,message_id) VALUES ('NULL','{}',NOW(),NOW(),'{}','{}')".format(request.form['commentText'],session['loggedIn'][len(session['loggedIn'])-1]['id'],request.form['comment'])
	mysql.run_mysql_query(query)
	return redirect('/wall')

app.run(debug=True)