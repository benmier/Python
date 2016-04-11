from system.core.model import Model
from flask import Flask, flash, redirect, render_template, session
from datetime import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
DATE_REGEX = re.compile(r'^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def register_user(self,user):
        errors = []
        if len(user['name'])<1 or len(user['birthday'])<1:
            errors.append('No field can be empty')
        elif not DATE_REGEX.match(user['birthday']):
            errors.append('Invalid birthday format')
        elif datetime.strptime(user['birthday'],'%Y-%m-%d').date()>=datetime.date(datetime.now()):
            errors.append('Birthday must be in the past')
        if len(user['password'])<8:
            errors.append('Password must be at least 8 characters')
        if user['password'] != user['confirm']:
            errors.append(('Passwords do not match'))
        if not EMAIL_REGEX.match(user['email']):
            errors.append("Invalid email")
        if errors == []:
            pwHash = self.bcrypt.generate_password_hash(user['password'])
            query = "INSERT INTO users (name,email,password,birthday,created_at,updated_at) VALUES (%s,%s,%s,%s,NOW(),NOW())"
            data = [user['name'],user['email'],pwHash,user['birthday']]
            self.db.query_db(query,data)
            user_login = self.db.query_db("SELECT * FROM users ORDER BY user_id desc LIMIT 1")
            session['name'] = user_login[0]['name']
            session['user_id'] = user_login[0]['user_id']
            return True
        else:
            for error in errors:
                flash(error)
            return False;

    def login_user(self,user):
        errors = []
        query = "SELECT * FROM users WHERE email='{}' LIMIT 1".format(user['email'])
        user_login = self.db.query_db(query)
        if user_login == []:
            errors.append("Unknown username")
        elif len(user_login[0]['email'])<1 or len(user_login[0]['password'])<1:
            errors.append('No field can be empty')
        elif not self.bcrypt.check_password_hash(user_login[0]['password'],user['password']):
            errors.append("Invalid password")
        if errors == []:
            session['name'] = user_login[0]['name']
            session['user_id'] = user_login[0]['user_id']
            return True
        else:
            for error in errors:
                flash(error)
            return False;

    def user_by_id(self,id):
        query = "SELECT * FROM users WHERE user_id='{}' LIMIT 1".format(id)
        return self.db.query_db(query)