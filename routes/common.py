from flask import Blueprint, jsonify, current_app
from flask_restful import Api


common_blueprint = Blueprint('common', __name__)
common_blueprint_api = Api(common_blueprint)

@common_blueprint.route('/')
def index():
    return jsonify({'message': 'Flask API is running'})
