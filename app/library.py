from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, User, Lending, Book

library = Blueprint('library', __name__)

@library.route('/<int:lib_id>')
@login_required
def main(lib_id):
    user = User.query.get(current_user.id)

    #return render_template('library.html',
    #                       libraries=libraries,
    #                       borrowings=borrowings,
    #                       lendings=lendings,
    #                       new_books=new_books,
    #                       username=user.username)

    return f"Hello, {user.username}! - Biblioteca: {lib_id}"
