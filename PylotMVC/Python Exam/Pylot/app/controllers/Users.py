from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('Travel')
        self.load_model('User')

    def index(self):
        return self.load_view('index.html')

    def register_user(self):
        new_user = {
            'name':request.form['name'],
            'username':request.form['username'],
            'password':request.form['password'],
            'confirm':request.form['confirm'],
        }
        if self.models['User'].register_user(new_user):
            return redirect('/travels')
        else:
            return  redirect('/main')

    def login(self):
        old_user = {
            'username':request.form['username2'],
            'password':request.form['password2'],
        }
        if self.models['User'].login_user(old_user):
            return redirect('/travels')
        else:
            return  redirect('/main')

    def logout(self):
        session.clear()
        return redirect('/')