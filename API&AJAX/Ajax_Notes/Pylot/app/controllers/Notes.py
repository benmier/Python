from system.core.controller import *
class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)
        self.load_model('Note')

    def index(self):
        notes = self.models['Note'].all()
        return self.load_view('index.html', notes=notes)

    def create(self):
        new_note = {
            'title': request.form['title']
        }
        self.models['Note'].create(new_note)
        return redirect('/')

    def update(self,id):
        note = {
            'descr': request.form['descr'],
            'note_id': id
        }
        self.models['Note'].update(note)
        return redirect('/')

    def delete(self,id):
        self.models['Note'].delete(id)
        return redirect('/')
