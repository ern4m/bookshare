from datetime import datetime, date
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import db, User, Library, Lending, Book

book = Blueprint('book', __name__)

@book.route('/<int:book_id>')
@login_required
def get(book_id):
    user = User.query.get(current_user.id)
    
    # book = Book.query.get(book_id)
    # Query to get the Book, Library, and User details
    query = (
        db.session.query(Book, Library.user_id)  # Select Book and Library.user_id
        .join(Library, Book.library_id == Library.id)  # Join Book and Library on library_id
        .filter(Book.id == book_id)  # Filter by the given book_id
        .first()  # Fetch the first result (since book_id is unique)
    )

    if query:
        book, owner_id = query
        return render_template('dashboard/book.html', 
                        user_id=user.id,
                        owner_id=owner_id,
                        book=book)
    
    return render_template('dashboard/book.html', 
                        user_id=user.id,
                        book=book)

@book.route('/create/<int:library_id>', methods=['GET', 'POST'])
@login_required
def create(library_id):
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        published_date = datetime.strptime(request.form['published_date'], "%Y-%m-%d")
        description = request.form['description']
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
            library_id=library_id,
            is_lent=is_lent,
            lending_id=lending_id
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Livro criado com sucesso!', 'success')
        return redirect(url_for('book.get', book_id=new_book.id))

    return render_template('dashboard/book_form.html', book=None, library_id=library_id)  # Passa `None` para criação

@book.route('/<int:book_id>/update', methods=['GET', 'POST'])
@login_required
def update(book_id):
    book = Book.query.get_or_404(book_id)

    # Não estamos tratando updates para bibliotecas que ainda nao foram criadas
    # ele so será visualizado caso a biblioteca seja criada ou alterando-o para uma biblioteca existente
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form['genre']
        book.published_date = datetime.strptime(request.form['published_date'], "%Y-%m-%d")
        book.description = request.form['description']
        book.library_id = request.form['library_id']
        book.is_lent = 'is_lent' in request.form
        book.lending_id = request.form['lending_id'] if request.form.get('lending_id') else None

        db.session.commit()

        flash('Livro atualizado com sucesso!', 'success')
        return redirect(url_for('book.get', book_id=book.id))

    return render_template('dashboard/book_form.html', book=book)

@book.route('/<int:book_id>/delete', methods=['POST'])
def delete(book_id):
    # Fetch the book from the database
    book = Book.query.get_or_404(book_id)

    # Get the library ID associated with the book
    library_id = book.library_id  # Assuming `library_id` is a foreign key in the Book model

    # Delete the book
    db.session.delete(book)
    db.session.commit()

    # Redirect to the library page
    return redirect(url_for('library.main', lib_id=library_id))