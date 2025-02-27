from flask import Blueprint, render_template, redirect, url_for, flash, session
from flask_login import login_required, current_user
from .models import db, User, Lending, Book, Library

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def main():
    return redirect(url_for('dashboard.libraries'))

@dashboard.route('/libraries')
@login_required
def libraries():
    user = User.query.get(current_user.id)

    others_libraries = Library.query\
                            .filter(Library.user_id != current_user.id)\
                            .order_by(Library.created_at.desc())\
                            .limit(10)\
                            .all()

    libraries = Library.query.filter_by(user_id=user.id).all()

    return render_template('dashboard/libraries.html',
                            libraries=libraries,
                            username=user.username,
                            others_libraries=others_libraries)

@dashboard.route('/borrowings')
@login_required
def borrowings():

    lendings_as_lender = (
        db.session.query(
            Book.title.label("book_title"),
            User.username.label("borrower_username"),  # Borrower name
            Lending.lend_date,               # Lend date
            Book.id,
            Lending.id.label("lending_id"),      # Lending ID
            Lending.return_date,             # Return date
        )
        .join(Book, Lending.book_id == Book.id)
        .join(User, Lending.borrower_id == User.id)  # Join for borrower
        .filter(Lending.lender_id == current_user.id)  # Filter by lender_id
        .all()  # Fetch all results
    )
    
    lendings_as_borrower = (
        db.session.query(
            Book.title.label("book_title"),
            User.username.label("lender_username"),   # Lender name
            Lending.lend_date, # Lend date
            Book.id,
            Lending.id.label("lending_id"),  # Lending ID
            Lending.return_date,             # Return date
        )
        .join(User, Lending.lender_id == User.id)  # Join for lender
        .join(Book, Lending.book_id == Book.id)
        .filter(Lending.borrower_id == current_user.id)  # Filter by borrower_id
        .all()  # Fetch all results
    )

    return render_template('dashboard/borrowings.html', lendings=lendings_as_lender, borrowings=lendings_as_borrower)
