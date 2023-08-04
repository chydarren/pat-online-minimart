'''
Author: Chua Han Yong Darren
Date: 04/08/2023 
Application: Pat's Online Minimart
File: __init__.py   
'''
# ========================================================================================================
# IMPORTS AND CONFIGURATIONS
# ========================================================================================================
# Import built-in modules 
import logging

# Import third-party modules
from flask import Blueprint, Flask, request, jsonify    # python -m pip install flask
from flask_sqlalchemy import SQLAlchemy                 # python -m pip install flask_sqlalchemy

# Configure logging
logging.basicConfig(level=logging.INFO)

# ========================================================================================================
# FLASK APP
# ========================================================================================================
# Create new Flask app instance 
app = Flask(__name__)

# ========================================================================================================
# DATABASE MODEL 
# ========================================================================================================
# Create store.db in the same directory as app.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'

# Create SQLAlchemy instance and pass in the Flask app instance
store = SQLAlchemy(app)

# ========================================================================================================
# API ENDPOINTS
# ========================================================================================================
# Import routes from app package
from app import routes




