from flask import Flask
from flask_caching import Cache

default_config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}


def get_flask_app_and_cache(config):
    """
    Given a cache type configures it and returns a flask app
    :return:
    """
    config = config or default_config
    app = Flask(__name__)
    # tell Flask to use the above defined config
    app.config.from_mapping(config)
    cache = Cache(app)
    return app, cache


def get_db_object():
    from pymongo import MongoClient

    client = MongoClient()
    return client.test_database