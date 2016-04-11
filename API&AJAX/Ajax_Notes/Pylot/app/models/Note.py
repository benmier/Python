from system.core.model import Model
class Note(Model):
    def __init__(self):
        super(Note, self).__init__()

    def all(self):
        query = "SELECT * FROM notes ORDER BY note_id desc"
        return self.db.query_db(query)

    def create(self,new_note):
        query = "INSERT INTO notes (title,descr,created_at,updated_at) VALUES (%s,'',NOW(),NOW())"
        data = [new_note['title']]
        return self.db.query_db(query,data)

    def update(self,note):
    	query = "UPDATE notes SET descr=%s,updated_at=NOW() WHERE note_id=%s"
    	data = [note['descr'],note['note_id']]
    	return self.db.query_db(query,data)

    def delete(self,id):
    	return self.db.query_db("DELETE FROM notes WHERE note_id='{}'".format(id))