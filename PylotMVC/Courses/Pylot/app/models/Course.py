from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()
    
    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM courses")

    def get_course_by_id(self, course_id):
        query = "SELECT * FROM courses WHERE id = %s"
        data = [course_id]
        return self.db.query_db(query, data)

    def delete_course_by_id(self, course_id):
        query = "DELETE FROM courses WHERE id = %s"
        data = [course_id]
        return self.db.query_db(query, data)

    def add_course(self,course):
        query = "INSERT INTO courses (title,description,created_at) VALUES (%s,%s,NOW())"
        data = [course['title'],course['description']]
        return self.db.query_db(query,data)

    def update_course(self,course):
        query = "UPDATE courses SET title=%s, description=%s WHERE id = %s"
        data = [course['title'],course['description'],course['id']]
        return self.db.query_db(query,data)


