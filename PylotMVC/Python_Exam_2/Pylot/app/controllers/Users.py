from system.core.controller import *
import datetime

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('Task')
        self.load_model('User')

    def index(self):
        return redirect('learn.codingdojo.com/m/3/3000')

    def register_user(self):
        new_user = {
            'name':request.form['name'],
            'email':request.form['email'],
            'password':request.form['password'],
            'confirm':request.form['confirm'],
            'birthday':request.form['birthday']
        }
        if self.models['User'].register_user(new_user):
            return redirect('/appointments')
        else:
            return  redirect('/main')

    def login(self):
        old_user = {
            'email':request.form['email2'],
            'password':request.form['password2'],
        }
        if self.models['User'].login_user(old_user):
            return redirect('/appointments')
        else:
            return  redirect('/main')

    def logout(self):
        session.clear()
        return redirect('/')