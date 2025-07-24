from extensions import db
from uuid import uuid4

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(), primary_key=True, default=str(uuid4()))
    usernam = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.Text())

    def __repr__(self):
        return f"<User {self.usernam}>"
    