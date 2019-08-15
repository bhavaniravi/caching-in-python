# from pymongo import MongoClient
# from base.data import user, events

# client = MongoClient()
# db = client.test_database
#
#
# def write_user():
#     collection = db['user']
#     collection.insert_many(user.values())
#
#
# def write_event():
#     collection = db['event']
#     collection.insert_many(events.values())
#
#
# def create_db_and_write_data():
#     write_user()
#     write_event()


def read_user(db, user_id):
    collection = db['user']
    return collection.find_one({"_id": user_id})


def read_event(db, event_id):
    collection = db['event']
    return collection.find_one({"_id": event_id})

