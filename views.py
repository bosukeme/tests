from flask import Blueprint, jsonify
from flask_restful import Api, Resource

from resources.user_resource import Registration, Login
from resources.user_resource import Templates, TemplatesUpdate

class Home(Resource):
    def get(self):
        return jsonify({
            "message": "Welcome to Sloovi Test!"
        })

user_bp = Blueprint("bot", __name__)

api = Api(user_bp)

api.add_resource(Home, '/')
api.add_resource(Registration, "/register")
api.add_resource(Login, "/login")
api.add_resource(Templates, "/template")
api.add_resource(TemplatesUpdate, "/template/<string:template_id>")
