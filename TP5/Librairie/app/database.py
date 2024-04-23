#from uuid import uuid4
from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from uuid import uuid4


engine = create_engine(
    #"sqlite:///data/database.sqlite", 
    "sqlite:///TP5\Librairie\data\database.sqlite", 
    echo=True
)

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

from app.models.book import Book 
from app.models.users import User



def create_database():
    Base.metadata.create_all(engine)

def clear_database():
    Base.metadata.clear()
    
def delete_database():
    Base.metadata.drop_all(engine)

def fill_users_db():    
    users_data = [
    {
        "id": str(uuid4()),
        "username": "john_doe",
        "firstname": "John",
        "name": "Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "admin": True,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "jane_smith",
        "firstname": "Jane",
        "name": "Smith",
        "email": "jane.smith@example.com",
        "password": "password456",
        "admin": False,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "bob_johnson",
        "firstname": "Bob",
        "name": "Johnson",
        "email": "bob.johnson@example.com",
        "password": "password789",
        "admin": False,
        "blocked": True
    },
    {
        "id": str(uuid4()),
        "username": "emily_clark",
        "firstname": "Emily",
        "name": "Clark",
        "email": "emily.clark@example.com",
        "password": "passwordabc",
        "admin": True,
        "blocked": True
    },
    {
        "id": str(uuid4()),
        "username": "michael_taylor",
        "firstname": "Michael",
        "name": "Taylor",
        "email": "michael.taylor@example.com",
        "password": "passworddef",
        "admin": False,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "susan_miller",
        "firstname": "Susan",
        "name": "Miller",
        "email": "susan.miller@example.com",
        "password": "passwordghi",
        "admin": False,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "david_anderson",
        "firstname": "David",
        "name": "Anderson",
        "email": "david.anderson@example.com",
        "password": "passwordjkl",
        "admin": True,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "amy_wilson",
        "firstname": "Amy",
        "name": "Wilson",
        "email": "amy.wilson@example.com",
        "password": "passwordmno",
        "admin": False,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "peter_brown",
        "firstname": "Peter",
        "name": "Brown",
        "email": "peter.brown@example.com",
        "password": "passwordpqr",
        "admin": False,
        "blocked": True
    },
    {
        "id": str(uuid4()),
        "username": "laura_evans",
        "firstname": "Laura",
        "name": "Evans",
        "email": "laura.evans@example.com",
        "password": "passwordstu",
        "admin": True,
        "blocked": False
    }
]
    
    with Session() as session:
        for user_data in users_data:
            user = User(
    id=user_data["id"],
    username=user_data["username"],
    firstname=user_data["firstname"],
    name=user_data["name"],
    email=user_data["email"],
    password=user_data["password"],
    admin=user_data["admin"],
    blocked=user_data["blocked"],)
            session.add(user)
        session.commit()


def fill_books_db():
    books_data = [
        {
            "id": str(uuid4()),
            "name": "La conquête de l'espace",
            "author": "Elon Musk",
            "editor": "Mc Donalds",
            "price": 20,
            "owner_id": str(uuid4())
        },
        {
            "id": str(uuid4()),
            "name": "Python pour les nuls",
            "author": "Benois Frénay",
            "editor": "Maison Frénay",
            "price": 25,
            "owner_id": str(uuid4())
        },
        {
            "id": str(uuid4()),
            "name": "Tchoupi à l'école",
            "author": "Erwin",
            "editor": "Kurtis Production",
            "price": 15,
            "owner_id": str(uuid4())
        },
        {
            "id": str(uuid4()),
            "name": "La poule et le lapin",
            "author": "Jean de La Fontaine",
            "editor": "Edition Hachette",
            "price": 30,
            "owner_id": str(uuid4())
        },
        {
            "id": str(uuid4()),
            "name": "Les bons, le con et le mouton",
            "author": "Ryan, Ilias",
            "editor": "Universal",
            "price": 40,
            "owner_id": str(uuid4())
        },
        {
            "id": str(uuid4()),
            "name": "100 recettes faciles maison",
            "author": "Agnès Dupont",
            "editor": "Test cuisine",
            "price": 35,
            "owner_id": str(uuid4())
        },
        {
            "id": str(uuid4()),
            "name": "Encyclopédie du football",
            "author": "Kiki Mbappe",
            "editor": "Le Football Il a Changé",
            "price": 50,
            "owner_id": str(uuid4())
        }
    ]

    with Session() as session:
        for book_data in books_data:
            book = Book(**book_data)
            session.add(book)
        session.commit()

"""bookstore = {
    "books" : 
        [
    {
        "id": str(uuid4()),
        "name" : "La conquête de l'espace",
        "author" : "Elon Musk",
        "editor" : "Mc Donalds"
    },
    {
        "id": str(uuid4()),
        "name" : "Python pour les nuls",
        "author" : "Benois Frénay",
        "editor" : "Maison Frénay"
    },
    {
        "id": str(uuid4()),
        "name" : "Tchoupi à l'école",
        "author" : "Erwin",
        "editor" : "Kurtis Production"
    },
    {
        "id": str(uuid4()),
        "name" : "La poule et le lapin",
        "author" : "Jean de La Fontaine",
        "editor" : "Edition Hachette"
    },
    {
        "id": str(uuid4()),
        "name" : "Les bons, le con et le mouton",
        "author" : "Ryan, Ilias",
        "editor" : "Universal"
    },
    {
        "id": str(uuid4()),
        "name" : "100 recettes faciles maison",
        "author" : "Agnès Dupont",
        "editor" : "Test cuisine"
    },
    {
        "id": str(uuid4()),
        "name" : "Encyclopédie du football",
        "author" : "Kiki Mbappe",
        "editor" : "Le Football Il a Changé"
    }
    ],
    "users": [
        {
            "id": str(uuid4()),
            "username": "johndu77",
            "firstname" : "John",
            "name" : "Wick",
            "password": "john_password",    
            "email": "John.Wick@gmail.com",
            "admin": True
        },
        {
            "id": str(uuid4()),
            "username": "stkiller6972",
            "firstname" : "Steve",
            "name" : "Jobs",
            "password": "steve_password",
            "email": "Steve.Jobs@gmail.com",
            "admin": False
        },
    ]
}"""



bigUser = {}