from collections import defaultdict
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import db, User, Lending, Book, Library

library = Blueprint('library', __name__)

mock_library = {
    "id": 1,
    "name": "Central City Library",
    "user_id": 101
}

@library.route('/<int:lib_id>')
@login_required
def main(lib_id):
    user = User.query.get(current_user.id)
    library = Library.query.get(lib_id)
    books = get_books_grouped_by_genre(library.id)
    return render_template('dashboard/library.html', 
                            username=user.username,
                            library=library,
                            books_by_genre=books)
    
@library.route('<int:library_id>', methods=['GET'])
@login_required
def get(library_id):
    library = Library.query.get_or_404(library_id)
    return render_template('dashboard/library_form.html', library=library)

@library.route('create', methods=['GET', 'POST'])
@login_required
def create():
    user = User.query.get(current_user.id)
    if request.method == 'POST':
        name = request.form['name']
        
        if not name:
            flash('All fields are required!', 'danger')
            return redirect(url_for('library.create_library'))
        
        new_library = Library(name=name, user_id=user.id)
        db.session.add(new_library)
        db.session.commit()
        flash('Library created successfully!', 'success')
        return redirect(url_for('library.get', library_id=new_library.id))
    
    return render_template('dashboard/library_form.html')

@library.route('<int:library_id>/update', methods=['GET', 'POST'])
@login_required
def update(library_id):
    library = Library.query.get_or_404(library_id)
    
    if request.method == 'POST':
        library.name = request.form['name']
        library.user_id = request.form['user_id']
        
        db.session.commit()
        flash('Library updated successfully!', 'success')
        return redirect(url_for('library.get', library_id=library.id))
    
    return render_template('dashboard/library_form.html', library=mock_library)

## Utils

def get_books_grouped_by_genre(library_id):
    books = Book.query.filter_by(library_id=library_id).all()
    
    # Group books by genre using defaultdict
    grouped_books = defaultdict(list)
    for book in books:
        grouped_books[book.genre].append({
            "id": book.id,
            "title": book.title,
            "genre": book.genre,
            "author": book.author,
            "published_date": book.published_date.strftime("%Y-%m-%d"),
            "description": book.description,
            "is_lent": book.is_lent
        })
    
    # Convert dictionary values to a list of lists (arrays of arrays)
    return list(grouped_books.values())  # Returns a list of lists