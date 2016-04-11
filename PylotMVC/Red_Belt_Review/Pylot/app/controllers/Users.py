from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Book')
    def index(self):
        return self.load_view('login.html')

    def register(self):
        new_user = {
            'name':request.form['name'],
            'alias':request.form['alias'],
            'email':request.form['email'],
            'password':request.form['password'],
            'confirm':request.form['confirm'],
        }
        if self.models['User'].register_user(new_user):

            return redirect('/book')
        else:
            return  redirect('/')

    def login(self):
        old_user = {
            'email':request.form['email'],
            'password':request.form['password'],
        }
        if self.models['User'].login_user(old_user):
            return redirect('/book')
        else:
            return  redirect('/')

    def logout(self):
        session.clear()
        return redirect('/')

    def users(self,id):
        user_info = self.models['User'].all_user_info(id)
        books = self.models['Book'].books_with_reviews_for_user_id(id)
        return self.load_view('users/users.html', id=id, user_info=user_info, books=books)

