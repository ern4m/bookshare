from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(150), nullable=True)
    lastname = db.Column(db.String(150), nullable=True)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    # One to many: User -> Libraries
    libraries = db.relationship(
        'Library',
        backref='owner',
        lazy=True,
    )

    # Many to many: Friends(Users) -> Friends(Users)
    friends = db.relationship(
        'User',
        secondary='friendships',
        primaryjoin='User.id==Friendship.user_id',
        secondaryjoin='User.id==Friendship.friend_id',
        backref='friend_of',
    )

    # Many to many: Users -> Books
    lent_books = db.relationship(
        'Lending',
        foreign_keys='Lending.lender_id',
        backref=db.backref('lender', lazy=True),
        lazy=True,
    )

    borrowed_books = db.relationship(
        'Lending',
        foreign_keys='Lending.borrower_id',
        backref=db.backref('borrower', lazy=True),
        lazy=True,
    )
