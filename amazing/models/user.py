from amazing.lib.database import db


class User(db.Model):
    __tablename__ = 'user'

    id_ = db.Column('id', db.Integer, primary_key=True)

    name = db.Column(db.Unicode(length=255), nullable=False)
