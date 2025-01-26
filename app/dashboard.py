from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, User, Lending, Book

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def main():
    user = User.query.get(current_user.id)

    libraries = user.libraries

    borrowings = Lending.query.filter_by(borrower_id=user.id).all()
    lendings = Lending.query.filter_by(lender_id=user.id).all()

    new_books = Book.query.filter(Book.library_id.in_([library.id for library in libraries]),
                                   Book.lending_id == None,  # Not lent
                                   Book.is_lent == False,    # Not lent
                                   Book.id > 0).all()
    return render_template('dashboard.html',
                           libraries=libraries,
                           borrowings=borrowings,
                           lendings=lendings,
                           new_books=new_books,
                           username=user.username)
    # return f"Hello, {user.lent_books}! Welcome to your dashboard."

@dashboard.route('/libraries')
@login_required
def libraries():
    user = User.query.get(current_user.id)

    return render_template('libraries.html', username=user.username)

@dashboard.route('/borrowings')
@login_required
def borrowings():
    user = User.query.get(current_user.id)

    #return render_template('libraries.html', username=user.username)
    return f"Hello, {user.username}! Welcome to your borrowings."
