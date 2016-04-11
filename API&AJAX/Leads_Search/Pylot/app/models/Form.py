from system.core.model import Model
class Form(Model):
    def __init__(self):
        super(Form, self).__init__()

    def all(self):
        query = "SELECT id,first_name,last_name,email,LEFT(registered_datetime,10) AS registered_datetime FROM leads ORDER BY id"
        return self.db.query_db(query)

    def update(self,form):
        query = "SELECT id,first_name,last_name,email,LEFT(registered_datetime,10) AS registered_datetime FROM leads \
                    WHERE CONCAT(first_name,last_name) LIKE CONCAT('%',%s,'%') \
                    AND %s<=registered_datetime\
                    AND %s>=registered_datetime"
        data = [form['name'],form['from_date'],form['to_date']]
        return self.db.query_db(query,data)