from flask import Flask

def create_app():
    app = Flask(__name__)


    from app.routes.routes import bp as suplementos_bp
    app.register_blueprint(suplementos_bp)

    return app
