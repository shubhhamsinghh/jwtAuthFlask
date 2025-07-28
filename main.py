from flask import Flask, jsonify
from extensions import db, jwt
from auth import auth_bp
from users import user_bp


def create_app():

    app = Flask(__name__)

    app.config.from_prefixed_env()
    
    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp,url_prefix='/auth')
    app.register_blueprint(user_bp,url_prefix='/users')

    # additional claims
    @jwt.additional_claims_loader
    def additional_claims_callback(identity):
        if identity == "Shubham Singh":
            return {"is_staff": True}
        return {"is_staff": False}

    # jwt error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message" : "Token has expired", "error" : "token_expired"}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"message" : "Signature varification failed", "error" : "invalid_token"}), 401
    
    @jwt.unauthorized_loader
    def unauthorized_loader_callback(error):
        return jsonify({"message" : "Request doesn't contain valid token", "error" : "authorization_header"}), 401

    return app

