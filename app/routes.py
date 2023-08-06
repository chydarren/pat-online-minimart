'''
Author: Chua Han Yong Darren
Date: 04/08/2023 
Application: Pat's Online Minimart
File: routes.py 
'''
# ========================================================================================================
# IMPORTS AND CONFIGURATIONS
# ========================================================================================================
# Import built-in modules
import logging
import functools

# Import third-party modules 
from flask import render_template, Flask, request, jsonify, redirect, url_for                       # python -m pip install flask
from flask_login import LoginManager, login_user, logout_user, login_required, current_user         # python -m pip install flask-login
from werkzeug.security import check_password_hash                                                   # python -m pip install werkzeug

# Import instances and models
from app import app, storeDb
from app.models import Item, User

# HTTP status codes 
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_SERVER_ERROR = 500

# Other constants 
MAX_ITEM_NAME_LENGTH = 100
MAX_ITEM_DESCRIPTION_LENGTH = 200
MAX_USERNAME_LENGTH = 80
MAX_PASSWORD_LENGTH = 80
MIN_ITEM_PRICE = 0
MIN_ITEM_QUANTITY = 0

# ========================================================================================================
# HELPER FUNCTIONS FOR BACKEND API SERVER
# ========================================================================================================
'''
Gets the submitted item fields from the request data after server-side input validation.

@param data         A JSON object containing the item details.
@return             An Item object containing the item details.
'''
def getSubmittedItemFields(data): 
    # Get fields from request data 
    item_name = data.get('item_name')
    item_description = data.get('item_description')
    item_price = float(data.get('item_price'))
    item_quantity = int(data.get('item_quantity'))

    # Fields cannot be empty
    if not item_name or not item_description or not item_price or not item_quantity:
        return None
    # Fields must be of the correct type
    elif not isinstance(item_name, str) or not isinstance(item_description, str) or not isinstance(item_price, float) or not isinstance(item_quantity, int):
        return None
    # String fields must be within the correct length 
    elif len(item_name) > MAX_ITEM_NAME_LENGTH or len(item_description) > MAX_ITEM_DESCRIPTION_LENGTH:
        return None 
    # Numeric fields must be positive 
    elif item_price < MIN_ITEM_PRICE or item_quantity < MIN_ITEM_QUANTITY:
        return None
    
    return Item(item_name, item_description, item_price, item_quantity)

'''
Gets the submitted user fields after server-side input validation.

@param username    The username of the user.
@param password    The password of the user.
@return            A tuple containing the username and password of the user.
'''
def getSubmittedUserFields(username, password): 
    # Fields cannot be empty
    if not username or not password:
        return None
    # Fields must be of the correct type
    elif not isinstance(username, str) or not isinstance(password, str):
        return None
    # String fields must be within the correct length 
    elif len(username) > MAX_USERNAME_LENGTH or len(password) > MAX_PASSWORD_LENGTH:
        return None 
    
    return username, password

'''
Reads all items in the store.

@return             A list of dictionary (Item) objects.
@throws Exception   If failed to read items from the store.
'''
def readAllItems():
    try:
        # Query all items from the store
        items = Item.query.all()

        # Store the items in a list of dictionary (Item) objects 
        items_data = [{'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price, 'quantity': item.quantity} for item in items]
        
        logging.info('(CRUD) Items were successfully read from the store.')
        return jsonify(items_data)
    except Exception as e:
        logging.error('(CRUD) Failed to read items from the store: %s.', e)
        return jsonify({"error": "Failed to read items from the store"}), HTTP_INTERNAL_SERVER_ERROR
    
'''
Creates a new item in the store.

@param data         A JSON object containing the item details.
@return             A JSON object containing the success message and HTTP status code.
@throws Exception   If failed to create item in the store.
'''
def createItem(data):
    # Get fields from request data after server-side input validation
    new_item = getSubmittedItemFields(data)
    
    if new_item is None:
        logging.info('(CRUD) Failed to create item in the store: Invalid item fields.')
        return jsonify({"error": "Failed to create item in the store"}), HTTP_INTERNAL_SERVER_ERROR

    try:
        # Add the new item object to the store 
        storeDb.session.add(new_item)

        # Commit the changes to the database
        storeDb.session.commit()

        logging.info('(CRUD) Item was successfully created in the store.')
        return jsonify({"message": "Item created successfully in the store"}), HTTP_CREATED
    except Exception as e:
        # Rollback the changes to the database
        storeDb.session.rollback()

        logging.error('(CRUD) Failed to create item in the store: %s.', e)
        return jsonify({"error": "Failed to create item in the store"}), HTTP_INTERNAL_SERVER_ERROR

'''
Reads an item in the store.

@param itemId      The ID of the item to read.
@return             A JSON object containing the item details.
@throws Exception   If failed to read item from the store.
'''
def readItem(itemId):
    try:
        # Query a specific item from the store
        item = Item.query.get(itemId)

        if item:
            logging.info('(CRUD) Item was successfully read from the store.')
            return jsonify({'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price, 'quantity': item.quantity})
        else:
            logging.info('(CRUD) Item was not found in the store.')
            return jsonify({"error": "Item not found in the store"}), HTTP_NOT_FOUND
    except Exception as e:
        logging.error('(CRUD) Failed to read item from the store: %s.', e)
        return jsonify({"error": "Failed to retrieve item"}), HTTP_INTERNAL_SERVER_ERROR

'''
Updates an item in the store.

@param itemId      The ID of the item to update.
@param data         A JSON object containing the item details.
@return             A JSON object containing the success message and HTTP status code.
@throws Exception   If failed to update item in the store.
'''
def updateItem(itemId, data):
    try:
        # Get the item with the specified ID
        item = Item.query.get(itemId)
        if item:
            new_item = getSubmittedItemFields(data)

            if new_item is None:
                logging.info('(CRUD) Failed to update item in the store: Invalid new item fields.')
                return jsonify({"error": "Failed to updat item in the store"}), HTTP_INTERNAL_SERVER_ERROR

            item.name = new_item.name
            item.description = new_item.description
            item.price = new_item.price
            item.quantity = new_item.quantity
            
            # Commit the changes to the database
            storeDb.session.commit()

            logging.info('(CRUD) Item was successfully updated in the store.')
            return jsonify({"message": "Item updated successfully in the store"}), HTTP_OK
        else:
            logging.info('(CRUD) Item was not found in the store.')
            return jsonify({"error": "Item not found in the store"}), HTTP_NOT_FOUND
    except Exception as e:
        # Rollback the changes to the database
        storeDb.session.rollback()

        logging.error('(CRUD) Failed to update item in the store: %s.', e)
        return jsonify({"error": "Failed to update item in the store"}), HTTP_INTERNAL_SERVER_ERROR
    
'''
Deletes an item in the store.

@param itemId      The ID of the item to delete.
@return             A JSON object containing the success message and HTTP status code.
@throws Exception   If failed to delete item from the store.
'''
def deleteItem(itemId):
    try:
        # Get the item with the specified ID
        item = Item.query.get(itemId)
        if item:
            # Delete the item from the database
            storeDb.session.delete(item)

            # Commit the changes to the database
            storeDb.session.commit()

            logging.info('(CRUD) Item was successfully deleted from the store.')
            return jsonify({"message": "Item deleted successfully from the store"}), HTTP_OK
        else:
            logging.info('(CRUD) Item was not found in the store.')
            return jsonify({"error": "Item not found in the store"}), HTTP_NOT_FOUND
    except Exception as e:
        # Rollback the changes to the database
        storeDb.session.rollback()

        logging.error('(CRUD) Failed to delete item from the store: %s.', e)
        return jsonify({"error": "Failed to delete item from the store"}), HTTP_INTERNAL_SERVER_ERROR

'''
Logs in a user by authenticating the username and password.

@param username     The username of the user.
@param password     The password of the user.
@return             True if the user is authenticated, otherwise False.
'''
def loginUser(username, password):
    username, password = getSubmittedUserFields(username, password) 

    if username is None or password is None:
        return False

    # Get the user with the specified username
    user = User.query.filter_by(username=username).first()

    # Check if the user exists and the password is correct
    if user and user.verifyPassword(password):
        login_user(user)
        return True
    else:
        return False

# ========================================================================================================
# ROUTES
# ========================================================================================================
'''
The default route.
'''
@app.route('/')
def index():
    # If user is logged in, redirect to store page
    if current_user.is_authenticated:
        return redirect(url_for('store'))
    else:
        return render_template('index.html', items=readAllItems().json)

'''
The login route which authenticate users from the login form in the index page.

@return     The store page if the user is authenticated, otherwise the index page.
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return redirect(url_for('index'))
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # If user is logged in, redirect to store page
        if loginUser(username, password):
            return redirect(url_for('store'))
        else:
            return redirect(url_for('index'))

'''
The store route which displays the store page.

@return     The store page if the user is authenticated.
'''
@app.route('/store')
@login_required
def store():
    return render_template('store.html', items=readAllItems().json)

'''
The logout route which logs out the user from the store page.
'''
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

'''
API item routes for CRUD operations. 
'''
@app.route('/item', methods=['GET', 'POST'])
@login_required
def items():
    if request.method == 'GET':
        return readAllItems()
    elif request.method == 'POST':
        return createItem(request.get_json())

@app.route('/item/<int:itemId>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def item(itemId):
    if request.method == 'GET':
        return readItem(itemId)
    elif request.method == 'PUT':
        return updateItem(itemId, request.get_json())
    elif request.method == 'DELETE':
        return deleteItem(itemId)