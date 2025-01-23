from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Import all models here
from .user import User
from .library import Library
from .book import Book
from .lending import Lending
from .friendship import Friendship
