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

    return render_template('dashboard/library.html', 
                            username=user.username,
                            library_name="Nome da Biblioteca")
    
@library.route('<int:library_id>', methods=['GET'])
def get(library_id):
    library = Library.query.get_or_404(library_id)
    return render_template('dashboard/library_form.html', library=mock_library)

@library.route('create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        
        if not name:
            flash('All fields are required!', 'danger')
            return redirect(url_for('library.create_library'))
        
        new_library = Library(name=name, user_id=0)
        db.session.add(new_library)
        db.session.commit()
        flash('Library created successfully!', 'success')
        return redirect(url_for('library.get', library_id=new_library.id))
    
    return render_template('dashboard/library_form.html')

@library.route('<int:library_id>/update', methods=['GET', 'POST'])
def update(library_id):
    library = Library.query.get_or_404(library_id)
    
    if request.method == 'POST':
        library.name = request.form['name']
        library.user_id = request.form['user_id']
        
        db.session.commit()
        flash('Library updated successfully!', 'success')
        return redirect(url_for('library.get', library_id=library.id))
    
    return render_template('dashboard/library_form.html', library=mock_library)