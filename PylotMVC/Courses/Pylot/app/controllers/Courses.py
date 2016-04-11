from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')

    def index(self):
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html',courses=courses)

    def destroy(self,id):
        getCourse = self.models['Course'].get_course_by_id(id)
        return self.load_view('/courses/show.html',getCourse=getCourse, id=id)

    def add(self):
        course_details = {'title':'{}'.format(request.form["title"]),'description':'{}'.format(request.form["description"])}
        self.models['Course'].add_course(course_details)
        return redirect('/')

    def delete(self, id):
        self.models['Course'].delete_course_by_id(id)
        return redirect('/')
