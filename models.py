"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):

    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.String, nullable = False)

    last_name = db.Column(db.String, nullable = False)

    image_url = db.Column(db.String)
        # maybe add a default image url
    
