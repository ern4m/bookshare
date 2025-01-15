from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to the modularized Flask app!"

@main.route('/dashboard')
@login_required
def dashboard():
    return f"Hello, {current_user.username}! Welcome to your dashboard."
