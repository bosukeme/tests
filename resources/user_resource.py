from flask_restful import Resource
from flask import request
from user_ops import register_user, login_user
from user_ops import ( 
    create_template, get_single_template, get_all_templates, update_template, delete_template)

from flask_jwt_extended import jwt_required

class Registration(Resource):
    def post(self):

        json_data = request.get_json()

        try:
            result = register_user(json_data)
            return result, 200

        except Exception as e:
            return {
                'status': 'failed',
                "message": str(e)
                }, 500



class Login(Resource):
    def post(self):
        json_data = request.get_json()

        try:
            result = login_user(json_data)
            return result, 200

        except Exception as e:
            return {
                'status': 'failed',
                "message": str(e)
                }, 500



    
class Templates(Resource):

    @jwt_required()
    def post(self):
        json_data = request.get_json()

        try:
            result = create_template(json_data)
            return result, 200

        except Exception as e:
            return {
                'status': 'failed',
                "message": str("Cross check the Access Token"),
                "Token Error": "Cross check the Access Token"
                }, 500

    @jwt_required()
    def get(self):
        try:
            result = get_all_templates()
            return result, 200

        except Exception as e:
            return {
                'status': 'failed',
                "message": str(e),
                "Token Error": "Cross check the Access Token"
                }, 500

    
    
class TemplatesUpdate(Resource):
    @jwt_required()
    def get(self, template_id):
        try:
            result = get_single_template(template_id)
            return result, 200

        except Exception as e:
            return {
                'status': 'failed',
                "message": str(e),
                "Token Error": "Cross check the Access Token"
                }, 500

    @jwt_required()
    def put(self, template_id):
        try:
            json_data = request.get_json()
            result = update_template(json_data, template_id)
            return result, 200

        except Exception as e:
            return {
                'status': 'failed',
                "message": str(e),
                "Token Error": "Cross check the Access Token"
                }, 500

    @jwt_required()
    def delete(self, template_id):
        try:
            result = delete_template(template_id)
            return result, 200

        except Exception as e:
            return {
                'status': 'failed',
                "message": str(e),
                "Token Error": "Cross check the Access Token"
                }, 500

