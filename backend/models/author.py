from db import db


class Author(db.Model):
    __tablename__ = "Author"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    books = db.relationship("Book", backref="Author", cascade="all, delete-orphan")

    def __init__(self, first_name, last_name, books):
        self.first_name = first_name
        self.last_name = last_name
        self.books = books

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return "<Author %d>" % self.id
