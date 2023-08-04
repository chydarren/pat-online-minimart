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
from flask import Flask, request, jsonify

# Import instances and models
from app import app, store
from app.models import Item

# ========================================================================================================
# ROUTES
# ========================================================================================================
@app.route('/')
def index():
    return 'Welcome to Uncle Pat\'s app Online Store!'