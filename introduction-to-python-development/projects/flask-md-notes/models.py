from flask_sqlalchemy import SQLAlchemy
from mistune import markdown

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    notes = db.relationship(
            'Note',
            # means notes.author() will return the User who made the note
            backref='author', 
            # finding a user will not automatically query for all notes. This query has to be made explicitly.
            lazy=True 
    )

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200)) 
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    user_id = db.Column(
            db.Integer, 
            # ensures that a user object with the given ID must already exist in the database 
            # in order for the note to be associated with them.
            db.ForeignKey('user.id'), 
            nullable=False
    )

    @property
    def body_html(self):
        return markdown(self.body)
