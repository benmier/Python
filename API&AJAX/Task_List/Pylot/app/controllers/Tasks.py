from system.core.controller import *
class Tasks(Controller):
    def __init__(self, action):
        super(Tasks, self).__init__(action)
        self.load_model('Task')

    def index(self):
        task = self.models['Task'].all()
        return self.load_view('index.html', tasks=task)

    def create(self):
        new_task = {
            'name': request.form['name']
        }
        self.models['Task'].create(new_task)
        return redirect('/')

    def update(self,id):
        task = {
            'name': request.form['name'],
            'task_id': id
        }
        self.models['Task'].update(task)
        return redirect('/')

    def delete(self,id):
        self.models['Task'].delete(id)
        return redirect('/')
