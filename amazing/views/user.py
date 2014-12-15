from werkzeug.exceptions import NotFound

from flask import jsonify
from flask import request
from flask.ext.classy import FlaskView

from amazing.lib.database import db
from amazing.models.user import User


class UserView(FlaskView):
    def index(self):
        users = db.session.query(User).all()
        return jsonify(data=[
            { 'id': user.id_, 'name': user.name } for user in users
            ])

    def get(self, id_):
        user = db.session.query(User).filter(User.id_ == id_).first()
        if not user:
            raise NotFound

        return jsonify(id=user.id_, name=user.name)

    def post(self):
        user = User(name=request.json.get('name'))
        db.session.add(user)
        db.session.commit()
        return self.get(user.id_)

    def put(self, id_):
        user = db.session.query(User).filter(User.id_ == id_).first()
        if not user:
            raise NotFound
        user.name = request.json.get('name')
        db.session.add(user)
        db.session.commit()
        return self.get(id_)

    def delete(self, id_):
        user = db.session.query(User).filter(User.id_ == id_).first()
        if not user:
            raise NotFound
        db.session.delete(user)
        db.session.commit()
        return jsonify()
