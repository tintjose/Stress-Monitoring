
import os
from flask import Flask
from .controllers import *
from .models import *
from .core import db, security
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_security import MongoEngineUserDatastore

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db.init_app(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

user_datastore = MongoEngineUserDatastore(db, User, Role)

security.init_app(app, user_datastore)

app.register_blueprint(auth_controller, url_prefix='/api/auth')
app.register_blueprint(test_controller, url_prefix='/api/test')

@app.route('/hello')
def home():
    return jsonify({'message': 'Hello'})

@app.after_request
def apply_headers(response):
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    if(os.environ['SERVER_PROD']!=None):
        app.run(host='0.0.0.0', port=80)
    else:
        app.run()
