from datetime import datetime, date
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import db, User, Lending, Book

book = Blueprint('book', __name__)

mock_book = {
    "id": 0,
    "title": "The Great Adventure",
    "author": "John Doe",
    "genre": "Fantasy",
    "published_date": date(2020, 5, 15),
    "description": "An epic fantasy novel about an unlikely hero who sets out to save the world.",
    "library_id": 1,  # Assuming this book belongs to a library with ID 1
    "is_lent": False,  # This book is currently not lent out
    "lending_id": None  # No lending record associated
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
                        book=mock_book)

@book.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        published_date = datetime.strptime(request.form['published_date'], "%Y-%m-%d")
        description = request.form['description']
        library_id = 0,#request.form['library_id']
        is_lent = 'is_lent' in request.form
        lending_id = request.form['lending_id'] if request.form.get('lending_id') else None

        if not title or not author or not genre or not published_date or not description or not library_id:
            flash('Todos os campos obrigatórios devem ser preenchidos!', 'danger')
            return redirect(url_for('book.create_book'))

        new_book = Book(
            title=title,
            author=author,
            genre=genre,
            published_date=published_date,
            description=description,
            library_id= 0,#library_id,
            is_lent=is_lent,
            lending_id=lending_id
        )
        # db.session.add(new_book)
        # db.session.commit()
        flash('Livro criado com sucesso!', 'success')
        return redirect(url_for('book.get', book_id=0))#new_book.id))

    return render_template('dashboard/book_form.html', book=None)  # Passa `None` para criação

@book.route('/<int:book_id>/update', methods=['GET', 'POST'])
@login_required
def update(book_id):
    # book = Book.query.get_or_404(book_id)

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form['genre']
        book.published_date = datetime.strptime(request.form['published_date'], "%Y-%m-%d")
        book.description = request.form['description']
        book.library_id = 0 #request.form['library_id']
        book.is_lent = 'is_lent' in request.form
        book.lending_id = request.form['lending_id'] if request.form.get('lending_id') else None

        # db.session.commit()
        flash('Livro atualizado com sucesso!', 'success')
        return redirect(url_for('book.get', book_id=0))#new_book.id))

    return render_template('dashboard/book_form.html', book=mock_book)

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
    return redirect(url_for('library.main', lib_id=mock_book['lib_id']))