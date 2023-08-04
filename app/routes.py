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

# Import third-party modules 
from flask import render_template, Flask, request, jsonify

# Import instances and models
from app import app, store
from app.models import Item

# HTTP status codes 
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_SERVER_ERROR = 500

# ========================================================================================================
# HELPER FUNCTIONS FOR BACKEND API SERVER
# ========================================================================================================
'''
Reads all items in the store.

@return             A list of dictionary (Item) objects.
@throws Exception   If failed to read items from the store.
'''
def read_all_items():
    try:
        # Query all items from the store
        items = Item.query.all()

        # Store the items in a list of dictionary (Item) objects 
        items_data = [{'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price, 'quantity': item.quantity} for item in items]
        return jsonify(items_data)
    except Exception as e:
        return jsonify({"error": "Failed to read items from the store"}), HTTP_INTERNAL_SERVER_ERROR
    
'''
Creates a new item in the store.

@param data         A JSON object containing the item details.
@return             A JSON object containing the success message and HTTP status code.
@throws Exception   If failed to create item in the store.
'''
def create_item(data):
    # Get fields from request data 
    item_name = data.get('item_name')
    item_description = data.get('item_description')
    item_price = data.get('item_price')
    item_quantity = data.get('item_quantity')
        
    # Create a new item object
    new_item = Item(item_name, item_description, item_price, item_quantity)

    try:
        # Add the new item object to the store 
        store.session.add(new_item)

        # Commit the changes to the database
        store.session.commit()

        return jsonify({"message": "Item created successfully in the store"}), HTTP_CREATED
    except Exception as e:
        # Rollback the changes to the database
        store.session.rollback()
        return jsonify({"error": "Failed to create item in the store"}), HTTP_INTERNAL_SERVER_ERROR

'''
Reads an item in the store.

@param item_id      The ID of the item to read.
@return             A JSON object containing the item details.
@throws Exception   If failed to read item from the store.
'''
def read_item(item_id):
    try:
        # Query a specific item from the store
        item = Item.query.get(item_id)

        if item:
            # Store the item in a dictionary (Item) object
            return jsonify({'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price, 'quantity': item.quantity})
        else:
            return jsonify({"error": "Item not found in the store"}), HTTP_NOT_FOUND
    except Exception as e:
        return jsonify({"error": "Failed to retrieve item"}), HTTP_INTERNAL_SERVER_ERROR

'''
Updates an item in the store.

@param item_id      The ID of the item to update.
@param data         A JSON object containing the item details.
@return             A JSON object containing the success message and HTTP status code.
@throws Exception   If failed to update item in the store.
'''
def update_item(item_id, data):
    try:
        # Get the item with the specified ID
        item = Item.query.get(item_id)
        if item:
            # Update the item object with the new data
            item.name = data.get('item_name')
            item.description = data.get('item_description')
            item.price = data.get('item_price')
            item.quantity = data.get('item_quantity')
            
            # Commit the changes to the database
            store.session.commit()
            return jsonify({"message": "Item updated successfully in the store"}), HTTP_OK
        else:
            return jsonify({"error": "Item not found in the store"}), HTTP_NOT_FOUND
    except Exception as e:
        # Rollback the changes to the database
        store.session.rollback()
        return jsonify({"error": "Failed to update item in the store"}), HTTP_INTERNAL_SERVER_ERROR
    
'''
Deletes an item in the store.

@param item_id      The ID of the item to delete.
@return             A JSON object containing the success message and HTTP status code.
@throws Exception   If failed to delete item from the store.
'''
def delete_item(item_id):
    try:
        # Get the item with the specified ID
        item = Item.query.get(item_id)
        if item:
            # Delete the item from the database
            store.session.delete(item)

            # Commit the changes to the database
            store.session.commit()
            return jsonify({"message": "Item deleted successfully from the store"}), HTTP_OK
        else:
            return jsonify({"error": "Item not found in the store"}), HTTP_NOT_FOUND
    except Exception as e:
        # Rollback the changes to the database
        store.session.rollback()
        return jsonify({"error": "Failed to delete item from the store"}), HTTP_INTERNAL_SERVER_ERROR

# ========================================================================================================
# ROUTES
# ========================================================================================================
@app.route('/')
def index():
    return render_template('index.html', items=read_all_items().json)

@app.route('/item', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        return read_all_items()
    elif request.method == 'POST':
        logging.info(request.get_json())
        return create_item(request.get_json())

@app.route('/item/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def item(item_id):
    if request.method == 'GET':
        return read_item(item_id)
    elif request.method == 'PUT':
        return update_item(item_id, request.get_json())
    elif request.method == 'DELETE':
        return delete_item(item_id)
