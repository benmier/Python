from system.core.model import Model
from flask import Flask, flash, redirect, render_template, session
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
NAME_REGEX = re.compile(r'\d')

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def register_user(self,user):
        errors = []
        if len(user['first_name'])<1 or len(user['last_name'])<1:
            errors.append('No field can be empty')
        if len(user['password'])<8:
            errors.append('Password must be at least 8 characters')
        if user['password'] != user['confirm']:
            errors.append(('Passwords do not match'))
        if not EMAIL_REGEX.match(user['email']):
            errors.append("Invalid email")
        if NAME_REGEX.search(user['first_name']) or NAME_REGEX.search(user['last_name']):
            errors.append("Name cannot contain numbers")
        if errors == []:
            pwHash = self.bcrypt.generate_password_hash(user['password'])
            query = "INSERT INTO users (first_name,last_name,email,user_level,password,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,NOW(),NOW())"
            data = [user['first_name'],user['last_name'],user['email'],user['user_level'],pwHash]
            self.db.query_db(query,data)
            user_login = self.db.query_db("SELECT * FROM users ORDER BY user_id desc LIMIT 1")
            if user_login[0]['user_id']==1:
                self.db.query_db("UPDATE users SET user_level=9 WHERE user_id='{}'".format(user_login[0]['user_id']))
            session['first_name'] = user_login[0]['first_name']
            session['last_name'] = user_login[0]['last_name']
            session['user_id'] = user_login[0]['user_id']
            return True
        else:
            for error in errors:
                flash(error)
            return False;

    def login_user(self,user):
        query = "SELECT * FROM users WHERE email='{}' LIMIT 1".format(user['email'])
        user_login = self.db.query_db(query)
        if user_login == []:
            flash("Unknown email")
        elif not self.bcrypt.check_password_hash(user_login[0]['password'],user['password']):
            flash("Invalid password")
        else:
            session['first_name'] = user_login[0]['first_name']
            session['last_name'] = user_login[0]['last_name']
            session['user_id'] = user_login[0]['user_id']
            return True
        return redirect('/')

    def user_by_id(self,id):
        query = "SELECT * FROM users WHERE user_id='{}' LIMIT 1".format(id)
        return self.db.query_db(query)

    