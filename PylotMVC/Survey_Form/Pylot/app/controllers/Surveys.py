from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

    def index(self):
        return self.load_view('index.html')

    def process(self):
        session['name'] = request.form['name']
        session['dojo'] = request.form['dojo']
        session['lang'] = request.form['lang']
        session['comment'] = request.form['comment']
        return redirect('/result')
        
    def result(self):
        return self.load_view('surveys/process.html')
