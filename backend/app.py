from flask import Flask
from app.api import route_blueprint
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register API blueprint
    app.register_blueprint(route_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
