from flask import Blueprint, render_template, redirect, url_for, flash
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

    libraries = Library.query.filter_by(user_id=user.id).all()
    print(libraries, user.id)

    return render_template('dashboard/libraries.html', libraries=libraries, username=user.username)

@dashboard.route('/borrowings')
@login_required
def borrowings():
    user = User.query.get(current_user.id)

    return render_template('dashboard/borrowings.html', username=user.username)
