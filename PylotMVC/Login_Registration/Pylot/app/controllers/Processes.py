from system.core.controller import *

class Processes(Controller):
    def __init__(self, action):
        super(Processes, self).__init__(action)
        self.load_model('Process')

    def index(self):
        
        return self.load_view('index.html')

    def process(self):
        user = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':request.form['password'],
            'confirm':request.form['confirm']
        }
        user_data = self.models['Process'].create(user)
        if user_data:
            session['first_name'] = user['first_name']
            session['email'] = user['email']
            session['status'] = "registered"
            return redirect('/success')
        else:
            return redirect('/')

    def login(self):
        user_login = {
            'email':request.form['email'],
            'password':request.form['password']
        }
        session['email'] = user_login['email']
        login = self.models['Process'].login(user_login)
        if login:
            session['status'] = "logged in"
            return redirect('/success')
        else:
            return redirect('/')

    def success(self):
        return self.load_view('/process/success.html')