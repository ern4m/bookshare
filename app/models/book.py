from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    library_id = db.Column(db.Integer, db.ForeignKey('library.id'), nullable=False)
    is_lent = db.Column(db.Boolean, default=False)
    lending_id = db.Column(db.Integer, db.ForeignKey('lending.id'), nullable=True)