from system.core.model import Model
class Task(Model):
    def __init__(self):
        super(Task, self).__init__()

    def all(self):
        query = "SELECT * FROM tasks ORDER BY task_id desc"
        return self.db.query_db(query)

    def create(self,new_task):
        query = "INSERT INTO tasks (name,created_at,updated_at) VALUES (%s,NOW(),NOW())"
        data = [new_task['name']]
        return self.db.query_db(query,data)

    def update(self,task):
    	query = "UPDATE tasks SET name=%s,updated_at=NOW() WHERE task_id=%s"
    	data = [task['name'],task['task_id']]
    	return self.db.query_db(query,data)

    def delete(self,id):
    	return self.db.query_db("DELETE FROM tasks WHERE task_id='{}'".format(id))