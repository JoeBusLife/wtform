"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ Pet object """
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    
    name = db.Column(db.Text,
                        nullable=False)
    
    species = db.Column(db.Text,
                        nullable=False)
                        
    photo_url = db.Column(db.Text)
    
    age = db.Column(db.Integer)
    
    notes = db.Column(db.Text)
    
    available = db.Column(db.Boolean,
                            nullable=False,
                            default=True)
    
    def __repr__(self):
        """ Show details of pet object """
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} photo_url={p.photo_url} age={p.age} notes_len={len(p.notes)} available={p.available}>"