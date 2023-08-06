'''
Author: Chua Han Yong Darren
Date: 06/08/2023 
Application: Pat's Online Minimart
File: config.py 
'''
# ========================================================================================================
# IMPORTS
# ========================================================================================================
# Import built-in modules
import secrets

# ========================================================================================================
# CONFIGURATIONS
# ========================================================================================================
# Create storeDb.db in the same directory as app.py
SQLALCHEMY_DATABASE_URI = 'sqlite:///storeDb.db'

# Set secret key for session
SECRET_KEY = secrets.token_urlsafe(16)