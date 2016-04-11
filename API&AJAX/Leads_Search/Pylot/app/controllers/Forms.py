from system.core.controller import *
import datetime

class Forms(Controller):
    def __init__(self, action):
        super(Forms, self).__init__(action)
        self.load_model('Form')

    def index(self):
        form = self.models['Form'].all()
        today = datetime.date.today().strftime('%Y-%m-%d')
        return self.load_view('index.html', forms=form, today=today)

    def update(self):
        print "*"*50
        update = {
            'name': request.form['name'],
            'from_date': request.form['from_date'],
            'to_date': request.form['to_date']
        }
        if len(update['from_date'])<1:
            update['from_date']='0000-01-01'
        if len(update['to_date'])<1:
            update['to_date']='9999-12-31'
        print update
        form = self.models['Form'].update(update)
        return self.load_view('partial.html', forms=form)