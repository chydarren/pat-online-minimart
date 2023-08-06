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
from app import storeDb, loginManager

# ========================================================================================================
# DATABASE MODELS
# ========================================================================================================
'''
Creates a model for Item. 

@param storeDb.Model: The base class for all models
'''
class Item(storeDb.Model): 
    id = storeDb.Column(storeDb.Integer, primary_key=True)
    name = storeDb.Column(storeDb.String(100), nullable=False)
    description = storeDb.Column(storeDb.String(200))
    price = storeDb.Column(storeDb.Float, nullable=False)
    quantity = storeDb.Column(storeDb.Integer, nullable=False)

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

'''
Creates a model for User, i.e. the Admin account(s). 

@param storeDb.Model:   The base class for all models.
@param UserMixin:       Default implementations for the methods that Flask-Login expects user objects to have.
'''
class User(storeDb.Model, UserMixin):
    # Map this model to the 'users' table 
    __tablename__ = 'users'
    
    id = storeDb.Column(storeDb.Integer, primary_key=True)
    username = storeDb.Column(storeDb.String(80), unique=True, nullable=False)
    password = storeDb.Column(storeDb.String(80), nullable=False)

    # Default constructor
    def __init__(self, username, password):
        # id is auto-generated and incremented
        self.username = username
        self.password = generate_password_hash(password)
    
    # Verify password
    def verifyPassword(self, password):
        return check_password_hash(self.password, password)
    