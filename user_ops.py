import json
from bson import ObjectId, json_util
from decouple import config as env_config
from flask_jwt_extended import create_access_token, jwt_required

from mongodb.mongo_util import (
    connect_to_mongo_db, get_record_details, save_to_mongo_db, update_record, delete_record)

MONGO_URL = env_config("MONGO_URL")





def initiate_mongo_db():
    ...

def register_user(user_data):
    email = user_data.get("email")
    search_query = {"email": email}

    collection = connect_to_mongo_db("users_db", "users_collection", MONGO_URL)

    result = get_record_details(search_query, collection)

    if result is None:
        save_to_mongo_db(user_data, collection)
        return {"Message": "User Registration Successful"}

    else:
        return {"Message": "User ALready Registered with that Email"}


def login_user(user_data):
    email = user_data.get("email")
    password = user_data.get("password")
    search_query = {"email": email}

    collection = connect_to_mongo_db("users_db", "users_collection", MONGO_URL)

    result = get_record_details(search_query, collection)
    password_in_db = result.get("password")
    first_name = result.get("first_name")

    if result and (password == password_in_db):
        access_token = create_access_token(identity=email)
        print(access_token)
        return {"Message": f"Welcome {first_name}",
                "access_token": access_token}

    elif result and (password != password_in_db):
        return {"Message": "Wrong Password. Try Again"}

    else:
        return {"Message": f"{email} is not registered"}


def create_template(template_data):

    template_name = template_data.get("template_name")

    collection = connect_to_mongo_db("users_db", "templates", MONGO_URL)
    search_query = {"template_name": template_name}

    result = get_record_details(search_query, collection)

    if result is None:
        save_to_mongo_db(template_data, collection)
        return {"message": "Template Successfully inserted"}

    else:
        return {"message": f"The Template, {template_name} already exists "}


def get_all_templates():
    collection = connect_to_mongo_db("users_db", "templates", MONGO_URL)
    all_records = list(collection.find({}))

    all_records = [json.loads(json_util.dumps(item)) for item in all_records]

    return all_records


def get_single_template(template_id):
    objInstance = ObjectId(template_id)
    search_query = {"_id": objInstance}
    
    collection = connect_to_mongo_db("users_db", "templates", MONGO_URL)
    result = get_record_details(search_query, collection)
    result = json.loads(json_util.dumps(result))
    return result

def update_template(template_data, template_id):
    objInstance = ObjectId(template_id)
    search_query = {"_id": objInstance}


    template_name = template_data.get("template_name")
    subject = template_data.get("subject")
    body = template_data.get("body")

    collection = connect_to_mongo_db("users_db", "templates", MONGO_URL)

    result = get_record_details(search_query, collection)

    if result:
        result['template_name'] = template_name
        result['subject'] = subject
        result['body'] = body

        new_values = {"$set" : result}
        update_record(collection, search_query, new_values)
        return {"message": "Template Successfully Updated"}


def delete_template(template_id):
    objInstance = ObjectId(template_id)
    search_query = {"_id": objInstance}

    collection = connect_to_mongo_db("users_db", "templates", MONGO_URL)


    result = get_record_details(search_query, collection)

    if result:
        delete_record(collection, result)
        return {"message": "Template Successfully Deleted"}


