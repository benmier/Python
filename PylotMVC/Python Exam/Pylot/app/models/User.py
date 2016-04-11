from system.core.model import Model
from flask import Flask, flash, redirect, render_template, session

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def register_user(self,user):
        errors = []
        if len(user['name'])<3 or len(user['username'])<3:
            errors.append('No field can be empty')
        if len(user['password'])<8:
            errors.append('Password must be at least 8 characters')
        if user['password'] != user['confirm']:
            errors.append(('Passwords do not match'))
        if errors == []:
            pwHash = self.bcrypt.generate_password_hash(user['password'])
            query = "INSERT INTO users (name,username,password,created_at,updated_at) VALUES (%s,%s,%s,NOW(),NOW())"
            data = [user['name'],user['username'],pwHash]
            self.db.query_db(query,data)
            user_login = self.db.query_db("SELECT * FROM users ORDER BY user_id desc LIMIT 1")
            session['name'] = user_login[0]['name']
            session['username'] = user_login[0]['username']
            session['user_id'] = user_login[0]['user_id']
            return True
        else:
            for error in errors:
                flash(error)
            return False;

    def login_user(self,user):
        errors = []
        query = "SELECT * FROM users WHERE username='{}' LIMIT 1".format(user['username'])
        user_login = self.db.query_db(query)
        if user_login == []:
            errors.append("Unknown username")
        elif len(user_login[0]['username'])<1 or len(user_login[0]['password'])<1:
            errors.append('No field can be empty')
        elif not self.bcrypt.check_password_hash(user_login[0]['password'],user['password']):
            errors.append("Invalid password")
        if errors == []:
            session['name'] = user_login[0]['name']
            session['username'] = user_login[0]['username']
            session['user_id'] = user_login[0]['user_id']
            return True
        else:
            for error in errors:
                flash(error)
            return False;

    def user_by_id(self,id):
        query = "SELECT * FROM users WHERE user_id='{}' LIMIT 1".format(id)
        return self.db.query_db(query)