from system.core.controller import *

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        self.load_model('Book')

    def index(self):
        reviews = self.models['Book'].latest_3_reviews()
        all_reviews = self.models['Book'].all_reviews()
        return self.load_view('books/books.html', reviews=reviews, all_reviews=all_reviews)

    def add(self):
        return self.load_view('books/add.html')

    def new_review(self):
        review = {
            'title':request.form['title'],
            'author':request.form['author'],
            'review':request.form['review'],
            'rating':request.form['rating'],
        }
        new_book = self.models['Book'].new_review(review)
        return redirect('/books/{}'.format(new_book))

    def books(self,id):
        reviews = self.models['Book'].book_by_id(id)
        title = reviews[0]['title']
        author = reviews[0]['author']
        book_id = reviews[0]['book_id'] 
        return self.load_view('books/book_page.html', id=book_id, reviews=reviews, title=title, author=author)

    def delete_review(self,book_id,review_id): 
        delete = self.models['Book'].delete_review(review_id)
        return redirect('/books/{}'.format(book_id))
