from pymongo import MongoClient


def get_record_details(search_dict, collection, find_one=True):
    """
        This searches through mongodb for a single record
    """
    try:
        query = collection.find_one(search_dict) if find_one else collection.find(search_dict)
        return query
    except Exception as e:
        print(e)
        return None


def insert_records(collection, record):
    """
        This inserts a single record to mongo db
    """
    try:
        collection.insert_one(record)
    except Exception as e:
        print(e)



def save_to_mongo_db(data, collection):
    """
        This saves the record to mongo db
    """
    insert_records(collection, data)
    cur = collection.count_documents({})
    print(f"we have {cur} entries")


def connect_to_mongo_db(db_name, collection_name, MONGO_URL):
    client = MongoClient(MONGO_URL)
    db = client[db_name]
    collection = db[collection_name]

    return collection


def update_record(collection, old, new):
    try:
        collection.update_one(old, new)
    except Exception as e:
        print(e)


def delete_record(collection, record):
    try:
        collection.delete_one(record)
    except Exception as e:
        print(e)
