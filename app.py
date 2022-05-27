from decouple import config as env_config
from flask import Flask
from flask_jwt_extended import JWTManager
from views import user_bp

SECRET_KEY = env_config("SECRET_KEY")


app = Flask(__name__)

app.secret_key = SECRET_KEY

jwt = JWTManager(app)
app.register_blueprint(user_bp)


if __name__=='__main__':
    app.run(port= 5000, debug=True)
