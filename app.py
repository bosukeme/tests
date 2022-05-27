from decouple import config as env_config
from flask import Flask
from flask_jwt_extended import JWTManager

SECRET_KEY = env_config("SECRET_KEY")

def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    from views import user_bp
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.logger.setLevel(app.config['LOG_LEVEL'])
    app.register_blueprint(user_bp)
    
    app.secret_key = SECRET_KEY
    


    JWTManager(app)

    return app





if __name__=="__main__":    
    app = create_app()
    app.run(port="5000")