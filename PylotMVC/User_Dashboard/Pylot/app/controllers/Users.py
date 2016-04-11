from system.core.controller import *
from datetime import datetime

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Message')

    def index(self):
        return self.load_view('index.html')
    def signin(self):
        return self.load_view('/new/login.html')
    def register(self):
        return self.load_view('/new/register.html')

    def register_user(self):
        new_user = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'user_level':1,
            'password':request.form['password'],
            'confirm':request.form['confirm'],
        }
        if self.models['User'].register_user(new_user):
            return redirect('/users/show/{}'.format(session['user_id']))
        else:
            return  redirect('/register')

    def login(self):
        old_user = {
            'email':request.form['email'],
            'password':request.form['password'],
        }
        if self.models['User'].login_user(old_user):
            return redirect('/users/show/{}'.format(session['user_id']))
        else:
            return  redirect('/signin')

    def logout(self):
        session.clear()
        return redirect('/')

    def show(self,id):
        user = self.models['User'].user_by_id(id)
        session['show_user_id'] = id
        messages = self.models['Message'].messages_via_postee(user)
        comments = self.models['Message'].comments_via_postee()
        return self.load_view('show/show.html', id=id, user=user[0], messages=messages, comments=comments)

