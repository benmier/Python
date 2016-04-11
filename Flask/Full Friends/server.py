from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector('friendsdb')
app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
	friends = mysql.fetch("SELECT * FROM friends")
	print friends
	return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['occupation'])
	mysql.run_mysql_query(query)
	return redirect('/')

@app.route('/friends/<friend_id>/edit', methods=['POST'])
def edit(friend_id):
	selectedFriend = mysql.fetch("SELECT * FROM friends WHERE id={}".format(friend_id))
	return render_template('user.html', friend_id=friend_id, selectedFriend=selectedFriend)

@app.route('/friends/<friend_id>/delete', methods=['POST'])
def delete(friend_id):
	query = "DELETE FROM friends WHERE id='{}'".format(request.form['delete'])
	mysql.run_mysql_query(query)
	return redirect('/')

@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
	query = "UPDATE friends SET first_name = '{}', last_name='{}', occupation='{}' WHERE id = {}".format(request.form['first_name'], request.form['last_name'], request.form['occupation'], friend_id)
	mysql.run_mysql_query(query)
	return redirect('/')

app.run(debug=True)