from datetime import datetime, date
from ..models import User, Library, Book, Lending  # Assuming the models are in a file named `models.py`

def db_populate(db):
    # Create users
    users = [
        User(
            username='john_doe',
            name='John',
            lastname='Doe',
            password='password123',
            email='john.doe@example.com'
        ),
        User(
            username='jane_smith',
            name='Jane',
            lastname='Smith',
            password='password456',
            email='jane.smith@example.com'
        ),
        User(
            username='alice_wonder',
            name='Alice',
            lastname='Wonder',
            password='password789',
            email='alice.wonder@example.com'
        )
    ]

    # Add users to the session
    db.session.add_all(users)
    db.session.commit()

    # Create libraries
    libraries = [
        Library(
            name='John\'s Personal Library',
            user_id=users[0].id
        ),
        Library(
            name='Jane\'s Book Collection',
            user_id=users[1].id
        ),
        Library(
            name='Alice\'s Reading Corner',
            user_id=users[2].id
        )
    ]

    # Add libraries to the session
    db.session.add_all(libraries)
    db.session.commit()

    # Create books
    books = [
        Book(
            title='To Kill a Mockingbird',
            author='Harper Lee',
            genre='Fiction',
            published_date=date(1960, 7, 11),
            description='A novel about the serious issues of rape and racial inequality.',
            library_id=libraries[0].id
        ),
        Book(
            title='1984',
            author='George Orwell',
            genre='Dystopian',
            published_date=date(1949, 6, 8),
            description='A dystopian novel set in Airstrip One, formerly Great Britain.',
            library_id=libraries[1].id
        ),
        Book(
            title='Pride and Prejudice',
            author='Jane Austen',
            genre='Romance',
            published_date=date(1813, 1, 28),
            description='A romantic novel of manners.',
            library_id=libraries[2].id
        ),
        Book(
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
            genre='Tragedy',
            published_date=date(1925, 4, 10),
            description='A story of the fabulously wealthy Jay Gatsby and his love for Daisy Buchanan.',
            library_id=libraries[0].id
        ),
        Book(
            title='Moby Dick',
            author='Herman Melville',
            genre='Adventure',
            published_date=date(1851, 10, 18),
            description='The voyage of the whaling ship Pequod, commanded by Captain Ahab.',
            library_id=libraries[1].id
        )
    ]

    # Add books to the session
    db.session.add_all(books)
    db.session.commit()

    # Create lending records
    lendings = [
        Lending(
            book_id=books[0].id,
            lender_id=users[0].id,
            borrower_id=users[1].id,
            lend_date=datetime(2023, 10, 1),
            return_date=datetime(2023, 10, 15)
        ),
        Lending(
            book_id=books[1].id,
            lender_id=users[1].id,
            borrower_id=users[2].id,
            lend_date=datetime(2023, 10, 5),
            return_date=None  # Book not yet returned
        ),
        Lending(
            book_id=books[2].id,
            lender_id=users[2].id,
            borrower_id=users[0].id,
            lend_date=datetime(2023, 10, 10),
            return_date=datetime(2023, 10, 20)
        )
    ]

    # Add lendings to the session
    db.session.add_all(lendings)
    db.session.commit()