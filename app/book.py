from flask import Blueprint, render_template, redirect, url_for, flash
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
def main(book_id):
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
