from . import db

class Library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # One to many: Library -> Books
    books = db.relationship(
        'Book',
        backref='library',
        lazy=True,
    )
