from system.core.controller import *
from flask import Flask,session

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)
        self.load_model('User')
        self.load_model('Message')

    def post_message(self):
        message = {'message':request.form['message']}
        self.models['Message'].post_message(message)
        return redirect('/users/show/{}'.format(session['show_user_id']))

    def post_comment(self,message_id):
        comment = {'comment':request.form['comment'], 'message_id':message_id}
        self.models['Message'].post_comment(comment)
        return redirect('/users/show/{}'.format(session['show_user_id']))