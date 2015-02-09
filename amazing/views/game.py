from werkzeug.exceptions import NotFound

from flask import jsonify
from flask import request
from flask.ext.classy import FlaskView

from amazing.lib.database import db
from amazing.models.game import Game


class GameView(FlaskView):
    def index(self):
        games = db.session.query(Game).all()
        return jsonify(data=[
            {
                'id': game.id_,
                'name': game.name,
                'owner_id': game.owner_id,
                'guest_id': game.guest_id
                } for game in games
            ])

    def get(self, id_):
        game = db.session.query(Game).filter(Game.id_ == id_).first()
        if not game:
            raise NotFound

        return jsonify(
            id=game.id_,
            name=game.name,
            owner_id=game.owner_id,
            guest_id=game.guest_id
            )

    def post(self):
        game = Game(
            name=request.json.get('name'),
            owner_id=request.json.get('owner_id'),
            guest_id=request.json.get('guest_id')
            )
        db.session.add(game)
        db.session.commit()
        return self.get(game.id_)

    def put(self, id_):
        game = db.session.query(Game).filter(Game.id == id_).first()

        if not game:
            raise NotFound

        game.name = request.json.get('name')
        game.owner_id = request.json.get('owner_id')
        game.guest_id = request.json.get('guest_id')
        db.session.add(game)
        db.session.commit()

        return self.get(game.id_)

    def delete(self, id_):
        game = db.session.query(Game).filter(Game.id_ == id_).first()

        if not game:
            raise NotFound

        db.session.delete(game)
        db.session.commit()

        return jsonify()
