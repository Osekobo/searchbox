from website import Flask


def create_app():
    app = Flask(__name__)  # file name
    app.config['SECRET_KEY'] = '123'  # production key secret
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
