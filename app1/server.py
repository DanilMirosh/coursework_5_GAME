from werkzeug.exceptions import HTTPException

from flask import Flask, jsonify


def base_server_error_handler(exception: HTTPException):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)


    return app
