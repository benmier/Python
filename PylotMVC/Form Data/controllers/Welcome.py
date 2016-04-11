from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

    def index(self):
        return self.load_view('index.html')

    def process(self):
        session['name'] = request.form['name']
        return redirect('welcome/success')

    def success(self):
        return  self.load_view('success.html', name=session['name'])
