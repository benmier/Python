from system.core.controller import *
import datetime

class Tasks(Controller):
	def __init__(self, action):
		super(Tasks, self).__init__(action)
		self.load_model('Task')
		self.load_model('User')

	def appointments(self):
		tasks = self.models['Task'].all_tasks()
		today_str = datetime.date.today().strftime("%B %d, %Y")
		today = datetime.date.today()
		return self.load_view('/show/appointments.html', tasks=tasks,  today_str=today_str, today=today)

	def add(self):
		task = {
			'date':request.form['date'],
			'time':request.form['time'],
			'title':request.form['title'],
		}
		new_task = self.models['Task'].add_task(task)
		return redirect('/appointments', )

	def edit(self,id):
		task = self.models['Task'].one_task(id)
		return self.load_view('/edit/edit.html', id=id, task=task)

	def edit_task(self,id):
		task = {
			'date':request.form['date'],
			'time':request.form['time'],
			'title':request.form['title'],
			'status':request.form['status'],
			'task_id':id
		}
		if self.models['Task'].edit_task(task):
			return redirect('/appointments')
		else:
			return redirect('/edit/{}'.format(id))

	def delete(self,id):
		self.models['Task'].delete(id)
		return redirect('/appointments')
