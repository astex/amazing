from amazing.views import user, game


def register(app):
    user.UserView.register(app, route_base='/user/')
    game.GameView.register(app, route_base='/game/')
