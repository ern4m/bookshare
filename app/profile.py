from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, Lending, Book

profile = Blueprint('profile', __name__)

@profile.route('/')
@login_required
def main():
    user = User.query.get(current_user.id)

    return render_template('profile/profile.html', user=user)


@profile.route('/update', methods=["POST", "GET"])
@login_required
def update():
    user = User.query.get(current_user.id)
    print(current_user)
    
    if request.method == "POST":
        # Get form data from the request
        username = request.form.get('username')
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        email = request.form.get('email')

        if not username:
            return flash("erro: campo Nome é obrigatório", 'danger')

        # Update the user's name and lastname if provided
        if name:
            user.name = name
        if lastname:
            user.lastname = lastname
        if username:
            user.username = username
        if email:
            # Check if the new email is already in use by another user
            existing_user_with_email = User.query.filter(User.email == email, User.id != user.id).first()
            if existing_user_with_email:
                return flash("error: Email já em uso", 'warning')
            user.email = email
            # Commit changes to the database
        db.session.commit()
        return redirect(url_for('profile.main'))

    return render_template('profile/update.html', user=user)

@profile.route('/change-password', methods=["POST", "GET"])
@login_required
def change_password():
    user = User.query.get(current_user.id)
    if request.method == "POST":
        # Get form data from the request
        psswd = request.form.get('psswd')
        new_psswd = request.form.get('new-psswd')
        confirm_new_psswd = request.form.get('confirm-new-psswd')

        # Validate required fields
        if not psswd or not new_psswd or not confirm_new_psswd:
            flash("All fields are required", "error")
            return redirect(url_for('profile.change_password'))

        # Verify the current password
        if not check_password_hash(user.password, psswd):
            flash("Current password is incorrect", "error")
            return redirect(url_for('profile.change_password'))

        # Check if new passwords match
        if new_psswd != confirm_new_psswd:
            flash("New passwords do not match", "error")
            return redirect(url_for('profile.change_password'))

        # Hash the new password
        hashed_password = generate_password_hash(new_psswd)  # Default method is pbkdf2:sha256
        user.password = hashed_password

        # Commit changes to the database
        db.session.commit()

        flash("Password updated successfully", "success")
        return redirect(url_for('profile.main'))

    return render_template('profile/change-password.html', user=user)