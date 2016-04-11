from system.core.model import Model
import re
from flask import Flask, flash, redirect, render_template, session
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
NAME_REGEX = re.compile(r'\d')

class Process(Model):
    def __init__(self):
        super(Process, self).__init__()
    
    def create(self,info):
        if len(info['first_name'])<2 or len(info['last_name'])<2:
            flash("Names must have at least 2 characters")
        elif NAME_REGEX.search(info['first_name']) or NAME_REGEX.search(info['last_name']):
            flash("Names must not contain numbers")
        elif not EMAIL_REGEX.match(info['email']):
            flash("Invalid email")
        elif len(info['password'])<8:
            flash("Password must be at least 8 characters")
        elif info['password'] != info['confirm']:
            flash("Passwords do not match")
        else:
            pwHash = self.bcrypt.generate_password_hash(info['password'])
            query = "INSERT INTO students (first_name,last_name,email,password,created_at,updated_at) VALUES ('{}','{}','{}','{}',NOW(),NOW())".format(info['first_name'],info['last_name'],info['email'],pwHash)
            self.db.query_db(query)
            return True
        return False

    def login(self,info):
        query = "SELECT * FROM students WHERE email='{}' LIMIT 1".format(session['email'])
        user_login = self.db.query_db(query)
        if user_login==[]:
            flash('Unknown email')
        elif not self.bcrypt.check_password_hash(user_login[0]['password'],info['password']):
            flash('Incorrect password') 
        else:
            session['first_name'] = user_login[0]['first_name']
            return True
        return redirect('/')
