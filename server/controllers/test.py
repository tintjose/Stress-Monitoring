
from flask import Blueprint, request, g, jsonify, abort, Response
from ..models import User, Role, Submission
from mongoengine import NotUniqueError
from http import HTTPStatus
from flask_security import auth_token_required, roles_required, current_user
import json
from datetime import datetime

test_controller = Blueprint('test', __name__)

# Example of a private endpoint
@test_controller.route('/myprivatestuff', methods=['GET'])
@auth_token_required
@roles_required('user')
def myPrompts():
    req_data = request.get_json()

    return jsonify(current_user)

#example if a public endpoint with parameter
@test_controller.route('/<urlparam>/submit', methods=['POST'])
def submitPrompt(urlparam):
    req_data = request.get_json()

    return jsonify({'param1': urlparam, 'param2': req_data['bodyparam']})

