from system.core.model import Model
from flask import Flask,session

class Book(Model):
    def __init__(self):
        super(Book, self).__init__()


    def latest_3_reviews(self):
        query = "SELECT * FROM reviews JOIN books ON books.book_id = reviews.review_book_id JOIN users ON users.user_id = reviews.review_user_id ORDER BY review_id desc LIMIT 3"
        return self.db.query_db(query)

    def all_reviews(self):
        query = "SELECT * FROM reviews JOIN books ON books.book_id = reviews.review_book_id JOIN users ON users.user_id = reviews.review_user_id GROUP BY review_book_id ORDER BY title"
        return self.db.query_db(query)

    def books_with_reviews_for_user_id(self,id):
        query = "SELECT * FROM reviews JOIN books ON book_id=review_book_id WHERE review_user_id='{}' GROUP BY title".format(id)
        return self.db.query_db(query)

    def new_review(self,book):
        query = "INSERT IGNORE INTO books (title,author) VALUES (%s,%s)" 
        data = [book['title'],book['author']]
        self.db.query_db(query,data)
        book_reviewed = self.db.query_db("SELECT book_id FROM books WHERE title='{}' AND author='{}' ORDER BY book_id LIMIT 1".format(book['title'],book['author']))
        query2 = "INSERT INTO reviews (review,rating,created_at,updated_at,review_user_id,review_book_id) VALUES (%s,%s,NOW(),NOW(),%s,%s)"
        data2 = [book['review'],book['rating'],session['user_id'],book_reviewed[0]['book_id']]
        self.db.query_db(query2,data2)
        return book_reviewed[0]['book_id']

    def book_by_id(self,id):
        query = "SELECT review,alias,title,rating,review_id,author,reviews.created_at,user_id,review_user_id,review_book_id,book_id FROM reviews JOIN books ON book_id = review_book_id JOIN users ON user_id = review_user_id WHERE review_book_id='{}' ORDER BY created_at desc".format(id)
        return self.db.query_db(query)

    def delete_review(self,review):
        query = "DELETE FROM reviews WHERE review_id = '{}'".format(review)
        return self.db.query_db(query)

