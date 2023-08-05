'''
Author: Chua Han Yong Darren
Date: 04/08/2023 
Application: Pat's Online Minimart
File: models.py 
'''
# ========================================================================================================
# IMPORTS AND CONFIGURATIONS
# ========================================================================================================
# Import third-party modules 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash    # python -m pip install werkzeug

# Import instances
from app import store, loginManager

# ========================================================================================================
# DATABASE MODELS
# ========================================================================================================
# Create a model for Item 
class Item(store.Model): 
    id = store.Column(store.Integer, primary_key=True)
    name = store.Column(store.String(100), nullable=False)
    description = store.Column(store.String(200))
    price = store.Column(store.Float, nullable=False)
    quantity = store.Column(store.Integer, nullable=False)

    # Default constructor
    def __init__(self, name, description, price, quantity):
        # id is auto-generated and incremented
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

@loginManager.user_loader
def getUser(userId):
    return User.query.get(userId)

# Create a model for User
# Note: In this application, only the admin user is required to login
class User(store.Model, UserMixin):
    __tablename__ = 'users'
    id = store.Column(store.Integer, primary_key=True)
    username = store.Column(store.String(80), unique=True, nullable=False)
    password = store.Column(store.String(80), nullable=False)

    # Default constructor
    def __init__(self, username, password):
        # id is auto-generated and incremented
        self.username = username
        self.password = generate_password_hash(password)
    
    # Verify password
    def verifyPassword(self, password):
        return check_password_hash(self.password, password)

    
