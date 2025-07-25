from flask import Flask
from extensions import db, jwt
from auth import auth_bp

def create_app():

    app = Flask(__name__)

    app.config.from_prefixed_env()
    
    db.init_app(app)
    jwt.init_app(app)


    app.register_blueprint(auth_bp,url_prefix='/auth')

    return app

