from base import get_flask_app_and_cache, get_db_object
from base.mongo_helper import read_event, read_user
from flask import jsonify

config = {'CACHE_TYPE': 'memcached',
          "CACHE_MEMCACHED_SERVERS": ['127.0.0.1:11211'],
          "DEBUG": True}
app, cache = get_flask_app_and_cache(config)
db = get_db_object()


@app.route("/")
@cache.cached(timeout=30)
def index():
    return "Hello"


@app.route("/user/<uid>")
@cache.cached(timeout=30)
def get_user(uid):

    try:
        return jsonify(read_user(db, uid))
    except KeyError as e:
        return jsonify({"Status": "Error", "message": str(e)})


@app.route("/event/<eid>")
@cache.cached(timeout=50)
def get_event(eid):
    try:
        return jsonify(read_event(db, eid))
    except KeyError as e:
        return jsonify({"Status": "Error", "message": str(e)})


if __name__ == '__main__':
    app.run(debug=True)