# models here
from src import db


class MyAwesomeModel(db.Model):
    """
        MyAwesomeModel
    """
    __tablename__ = "awesome_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120)))

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return '<MyAwesomeModel %r>' % self.id

    def save(self):
        db.session.add(self)
        db.session.commit()