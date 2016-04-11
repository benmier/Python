from system.core.model import Model
from flask import Flask,session

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()

    def messages_via_postee(self,user):
        query = "SELECT *,messages.created_at AS message_created_at FROM messages JOIN users ON user_id = message_poster_id WHERE message_postee_id='{}' ORDER BY message_id desc".format(session['show_user_id'])
        return self.db.query_db(query)

    def comments_via_postee(self):
        query = "SELECT *,comments.created_at AS comment_created_at FROM messages JOIN comments ON message_id = comment_message_id JOIN users ON user_id = comment_poster_id WHERE message_postee_id='{}' ORDER BY comment_id desc".format(session['show_user_id'])
        return self.db.query_db(query)

    def post_message(self,message):
        query = "INSERT INTO messages (message,message_poster_id,message_postee_id,created_at,updated_at) VALUES (%s,%s,%s,NOW(),NOW())"
        data = [message['message'],session['user_id'],session['show_user_id']]
        return self.db.query_db(query,data)

    def post_comment(self,comment):
        query = "INSERT INTO comments (comment,comment_message_id,comment_poster_id,created_at,updated_at) VALUES (%s,%s,%s,NOW(),NOW())"
        data = [comment['comment'],comment['message_id'],session['user_id']]
        return self.db.query_db(query,data)