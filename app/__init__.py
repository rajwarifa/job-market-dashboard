from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import views
    app.register_blueprint(views)

    return app
