from system.core.model import Model
from flask import Flask, flash, redirect, render_template, session
from datetime import datetime
import re
DATE_REGEX = re.compile(r'^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$')
TIME_REGEX = re.compile(r'^([01]\d|2[0-3]):?([0-5]\d):?([0-5]\d|2[0-9])$')

class Task(Model):
    def __init__(self):
        super(Task, self).__init__()
  
    def all_tasks(self):
        query = "SELECT * FROM tasks JOIN users on user_id=task_user_id ORDER BY date,time desc"
        return self.db.query_db(query)

    def one_task(self,id):
        task = self.db.query_db("SELECT * FROM tasks WHERE task_id='{}'".format(id))
        return task[0]

    def add_task(self,task):
        errors = []
        if len(task['date'])<1 or len(task['time'])<1 or len(task['title'])<1:
            errors.append('No field can be empty')
        elif not DATE_REGEX.match(task['date']):
            errors.append('Invalid date format')
        elif not TIME_REGEX.match(task['time']):
            errors.append('Invalid time format')
        if datetime.strptime(task['date'],'%Y-%m-%d').date()<datetime.date(datetime.now()):
            errors.append('Date cannot be in the past')
        all_tasks = self.db.query_db("SELECT * FROM tasks")
        for each in all_tasks:
            if task['date']==str(each['date']) and task['time']==str(each['time']):
                errors.append("Time conflict with task: {}".format(task['title']))
        if errors == []:
            query = "INSERT INTO tasks (status,date,time,title,task_user_id,task_created_at,task_updated_at) VALUES ('Pending',%s,%s,%s,%s,NOW(),NOW())"
            data = [task['date'],task['time'],task['title'],session['user_id']]
            self.db.query_db(query,data)
            new_task = self.db.query_db("SELECT * from tasks ORDER BY task_id desc LIMIT 1")
            return new_task[0]
        else:
            for error in errors:
                flash(error)
            return False;

    def edit_task(self,task):
        errors = []
        if len(task['date'])<1 or len(task['time'])<1 or len(task['title'])<1:
            errors.append('No field can be empty')
        elif datetime.strptime(task['date'],'%Y-%m-%d').date()<datetime.date(datetime.now()):
            errors.append('Date cannot be in the past')
        if not DATE_REGEX.match(task['date']):
            errors.append('Invalid date format')
        if not TIME_REGEX.match(task['time']):
            errors.append('Invalid time format')
        all_tasks = self.db.query_db("SELECT * FROM tasks")
        for each in all_tasks:
            if task['date']==each['date'] and task['time']==each['time']:
                errors.append("Time conflict with task: {}".format(task['title']))
        if errors == []:
            query = "UPDATE tasks SET status=%s,date=%s,time=%s,title=%s,task_updated_at=NOW() WHERE task_id=%s"
            data = [task['status'],task['date'],task['time'],task['title'],task['task_id']]
            self.db.query_db(query,data)
            return True
        else:
            for error in errors:
                flash(error)
            return False;

    def delete(self,id):
        return self.db.query_db("DELETE FROM tasks WHERE task_id='{}'".format(id))