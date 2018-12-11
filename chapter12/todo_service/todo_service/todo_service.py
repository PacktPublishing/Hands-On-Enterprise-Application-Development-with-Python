'''
File: todo_service.py
Description: The todo list management service
Author: Saurabh Badhwar
'''
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from jaeger_client import Config
from flask_opentracing import FlaskTracer
from opentracing_instrumentation.client_hooks import install_all_patches
import datetime
import requests

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

def init_tracer():
    """Initialize the tracing system."""

    config = Config(
        config={ # usually read from some yaml config
            'enabled': True,
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name='todo-service',
        validate=True,
    )
    return config.initialize_tracer()

install_all_patches()

flask_tracer = FlaskTracer(init_tracer, True, app)

db = SQLAlchemy(app)

user_service = app.config['USER_SERVICE_ENDPOINT']

from todo_service.models import List, Item

def check_required_fields(req_fields, input_list):
    """Check if the required fields are present inside the input list.

    Keyword arguments:
    req_fields -- The list of required fields
    input_list -- The list to validate for required fields

    Returns:
        Boolean
    """

    if all(field in req_fields for field in input_list):
        return True
    return False

@app.route('/ping', methods=['GET'])
def ping():
    """Ping application route."""
    return "PONG"

def validate_user(auth_token):
    """Validates a user and returns it user id.

    Keyword arguments:
    auth_token -- The authentication token to be used

    Returns:
        Integer
    """

    endpoint = user_service + '/auth/validate'
    resp = requests.post(endpoint, json={"auth_token": auth_token})
    if resp.status_code == 200:
        user = resp.json()
        user_id = user['user_id']
        return user_id
    else:
        return None

@app.route('/list/new', methods=['POST'])
def new_list():
    """Handle the creation of new list."""

    required_fields = ['auth_token', 'list_name']
    response = {}
    list_data = request.get_json()
    if not check_required_fields(required_fields, list_data.keys()):
        response['message'] = 'The required parameters are not provided'
        return jsonify(response), 400

    auth_token = list_data['auth_token']

    # Get the user id for the auth token provided
    user_id = validate_user(auth_token)

    # If the user is not valid, return an error
    if user_id is None:
        response['message'] = "Unable to login user. Please check the auth token"
        return jsonify(response), 400

    # User token is valid, let's create the list
    list_name = list_data['list_name']
    new_list = List(user_id=user_id, list_name=list_name)
    db.session.add(new_list)
    try:
        db.session.commit()
    except Exception:
        response['message'] = "Unable to create a new todo-list"
        return jsonify(response), 500
    response['message'] = "List created"
    return jsonify(response), 200

@app.route('/list/add_item', methods=['POST'])
def add_item():
    """Handle the addition of new items to the list."""

    required_fields = ['auth_token', 'list_name', 'items']
    response = {}
    list_data = request.get_json()

    if not check_required_fields(required_fields, list_data.keys()):
        response['message'] = "Required fields are missing"
        return jsonify(response), 400

    auth_token = list_data['auth_token']
    list_name = list_data['list_name']
    items = list_data['items']

    # Validate the user
    user_id = validate_user(auth_token)
    if user_id is None:
        response['message'] = "Unable to validate the user. Please check the auth token."
        return jsonify(response), 400

    # User is valid, get the todo list
    todo_list = List.query.filter_by(list_name=list_name).first()
    if not todo_list:
        response['message'] = "The list does not exist"
        return jsonify(response), 400

    list_id = todo_list.id

    # Remove the duplicates in the item list
    filtered_items = set(items)
    items_list = list(filtered_items)

    # Add the items to the database
    for item in items_list:
        item_obj = Item(list_id=list_id, item_name=item)
        db.session.add(item_obj)

    try:
        db.session.commit()
    except Exception:
        response['message'] = "Unable to add the items to the list"
        return jsonify(response), 500

    response['message'] = "Items saved to the todo list"
    return jsonify(response), 200

@app.route('/list/view', methods=['POST'])
def view_list():
    """Handle the display of the todo list."""

    required_fields = ['auth_token', 'list_name']
    response = {}
    list_data = request.get_json()

    if not check_required_fields(required_fields, list_data.keys()):
        response['message'] = "Required fields are missing"
        return jsonify(response), 400

    auth_token = list_data['auth_token']
    list_name = list_data['list_name']

    # Validate the user
    user_id = validate_user(auth_token)
    if user_id is None:
        response['message'] = "Unable to validate the user. Please check the auth token."
        return jsonify(response), 400

    # Get the details of the list
    todo_list = List.query.filter_by(user_id=user_id, list_name=list_name).first()
    if not todo_list:
        response['message'] = "Unable to find the list"
        return jsonify(response), 400

    # Gather the items from the list to return
    list_id = todo_list.id
    list_items = Item.query.filter_by(list_id=list_id).all()[:]
    response['list_name'] = todo_list['list_name']
    response['items'] = list_items

    return jsonify(response), 200

