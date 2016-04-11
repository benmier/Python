from system.core.model import Model
class Note(Model):
    def __init__(self):
        super(Note, self).__init__()

    def all(self):
        query = "SELECT * FROM notes ORDER BY note_id desc"
        return self.db.query_db(query)

    def create(self,new_note):
        query = "INSERT INTO notes (descr,created_at,updated_at) VALUES (%s,NOW(),NOW())"
        data = [new_note['descr']]
        return self.db.query_db(query,data)