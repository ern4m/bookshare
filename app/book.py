from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .models import db, User, Lending, Book

book = Blueprint('book', __name__)

book_data = {
    "id": 1,
    "lib_id": 0,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Fiction",
    "published_date": "1925",
    "description": "A novel set in the Jazz Age that tells the story of Jay Gatsby's unrequited love for Daisy Buchanan."
}

@book.route('/<int:book_id>')
@login_required
def get(book_id):
    user = User.query.get(current_user.id)

    #return render_template('library.html',
    #                       libraries=libraries,
    #                       borrowings=borrowings,
    #                       lendings=lendings,
    #                       new_books=new_books,
    #                       username=user.username)

    return render_template('dashboard/book.html', 
                        username=user.username,
                        book=book_data)
    
@book.route('/<int:book_id>/edit', methods=['GET', 'POST'])
@login_required
def update(book_id):
    # book = Book.query.get_or_404(book_id)  # Fetch the book from the database

    if request.method == 'POST':
        # Update the book with form data
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form['genre']
        book.published_date = request.form['published_date']
        book.description = request.form['description']

        # Save changes to the database
        db.session.commit()

        # Redirect to the book details page
        return redirect(url_for('book.get', book_id=book_data['id']))

    # Render the edit form with the current book data
    return render_template('dashboard/book_edit_form.html', book=book_data)

@book.route('/<int:book_id>/delete', methods=['POST'])
def delete(book_id):
    # Fetch the book from the database
    # book = Book.query.get_or_404(book_id)

    # Get the library ID associated with the book
    # library_id = book.library_id  # Assuming `library_id` is a foreign key in the Book model

    # Delete the book
    # db.session.delete(book)
    # db.session.commit()

    # Redirect to the library page
    return redirect(url_for('library.main', lib_id=book_data['lib_id']))