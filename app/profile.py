from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, User, Lending, Book

profile = Blueprint('profile', __name__)

@profile.route('/')
@login_required
def main():
    user = User.query.get(current_user.id)

    #return render_template('profile.html',
    #                       libraries=libraries,
    #                       borrowings=borrowings,
    #                       lendings=lendings,
    #                       new_books=new_books,
    #                       username=user.username)

    return render_template('profile.html', username=user.username, user=user)
