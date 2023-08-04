'''
Author: Chua Han Yong Darren
Date: 04/08/2023 
Application: Pat's Online Minimart
File: models.py 
'''
# ========================================================================================================
# IMPORTS AND CONFIGURATIONS
# ========================================================================================================
# Import instances
from app import store

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