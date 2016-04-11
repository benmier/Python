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
        if len(user['name'])<1 or len(user['alias'])<1 or len(user['email'])<1:
            errors.append('No field can be empty')
        if len(user['password'])<8:
            errors.append('Password must be at least 8 characters')
        if user['password'] != user['confirm']:
            errors.append(('Passwords do not match'))
        if not EMAIL_REGEX.match(user['email']):
            errors.append("Invalid email")
        if NAME_REGEX.search(user['name']) or NAME_REGEX.search(user['alias']):
            errors.append("Name cannot contain numbers")
        if errors == []:
            pwHash = self.bcrypt.generate_password_hash(user['password'])
            query = "INSERT INTO users (name,alias,email,password,created_at,updated_at) VALUES (%s,%s,%s,%s,NOW(),NOW())"
            data = [user['name'],user['alias'],user['email'],pwHash]
            self.db.query_db(query,data)
            user_login = self.db.query_db("SELECT * FROM users ORDER BY user_id desc LIMIT 1")
            session['alias'] = user_login[0]['alias']
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
            session['alias'] = user_login[0]['alias']
            session['user_id'] = user_login[0]['user_id']
            return True
        return redirect('/')

    def all_user_info(self,id):
        query = "SELECT *,COUNT(review_id) AS sum_reviews FROM users JOIN reviews ON user_id=review_user_id JOIN books on book_id=review_book_id WHERE user_id='{}' LIMIT 1".format(id)
        return self.db.query_db(query)