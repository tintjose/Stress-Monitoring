
from flask import Blueprint, request, jsonify, abort
from ..models import User, Role
from mongoengine import NotUniqueError
from http import HTTPStatus
from flask_security.utils import login_user

auth_controller = Blueprint('auth', __name__)

@auth_controller.route('/register', methods=['POST'])
def register():
    req_data = request.get_json()
    
    email = req_data['email']
    password = req_data['password']
    first_name = req_data['first_name']
    last_name = req_data['last_name']

    userRole = Role.objects.get(name="user")
    u = User(first_name=first_name, last_name=last_name, email=email, \
            password=password, active=True, roles=[userRole])
    try:
        u.save()
    except NotUniqueError:
        abort(HTTPStatus.CONFLICT)

    return jsonify(u)

@auth_controller.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()
    
    email = req_data['email']
    password = req_data['password']

    user = User.objects.get_or_404(email=email)
    if(user.password != password):
        abort(HTTPStatus.BAD_REQUEST)
    
    login_user(user)

    response = {
                'authentication_token': user.get_auth_token(),
                'id': str(user.id)
            }

    return jsonify(response)
