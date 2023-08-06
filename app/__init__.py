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
from flask_sqlalchemy import SQLAlchemy                 # python -m pip install flask-sqlalchemy
from flask_login import LoginManager                    # python -m pip install flask-login
from flask_wtf.csrf import CSRFProtect                  # python -m pip install flask-wtf

# Configure logging
logging.basicConfig(level=logging.INFO)

# ========================================================================================================
# FLASK APP
# ========================================================================================================
# Create new Flask app instance 
app = Flask(__name__)

# Set secret key for session
app.secret_key = 'test'

# CSRF protection
csrf = CSRFProtect(app)

# ========================================================================================================
# LOGIN MANAGER
# ========================================================================================================
# Create LoginManager instance
loginManager = LoginManager(app)
loginManager.login_view = '/'

# ========================================================================================================
# DATABASE MODEL 
# ========================================================================================================
# Create storeDb.db in the same directory as app.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storeDb.db'

# Create SQLAlchemy instance and pass in the Flask app instance
storeDb = SQLAlchemy(app)

# ========================================================================================================
# API ENDPOINTS
# ========================================================================================================
# Import routes from app package
from app import routes
