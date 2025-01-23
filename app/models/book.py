from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    library_id = db.Column(db.Integer, db.ForeignKey('library.id'), nullable=False)
    is_lent = db.Column(db.Boolean, default=False)

    # One to one: User -> User (has to be friends)
    lending_id = db.Column(db.Integer, db.ForeignKey('lending.id'), nullable=True)
