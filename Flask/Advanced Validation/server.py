from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'\d')
PASS_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email'])<1 or len(request.form['first'])<1 or len(request.form['last'])<1 or len(request.form['password'])<1 or len(request.form['confirm'])<1:
        flash("No fields can be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
    	flash("Invalid Email Address!")
    elif NAME_REGEX.search(request.form['first']) or NAME_REGEX.search(request.form['last']):
    	flash("Name fields cannot contain numbers!")
    elif len(request.form['password'])<=8:
    	flash("Password must be more than 8 characters!")
    elif str(request.form['password']) != str(request.form['confirm']):
    	flash("Passwords do not match!")
    elif not PASS_REGEX.match(request.form['password']):
    	flash("Password must contain at least 1 uppercase letter and 1 number!")
    else:
        flash("Thanks for submitting your information.")
    return redirect('/')

app.run(debug=True)