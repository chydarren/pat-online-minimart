'''
Author: Chua Han Yong Darren
Date: 04/08/2023 
Application: Pat's Online Minimart
File: run.py
'''
# ========================================================================================================
# IMPORTS AND CONFIGURATIONS
# ========================================================================================================
# Import built-in modules
import logging 

# Import instances and models
from app import app, storeDb
from app.models import User

# ========================================================================================================
# RUN FLASK APP
# ========================================================================================================
if __name__ == '__main__':
    with app.app_context():
        # Create database tables for data models
        storeDb.create_all()

        # For MVP, we will use a single pre-created admin account
        user = User.query.filter_by(username='unclepat').first()
        if user is None:
            # Create admin account and commit the changes to the database
            storeDb.session.add(User('unclepat', 'unclepat_2023_08'))
            storeDb.session.commit()

            logging.info('Created admin account: "unclepat".')
        else:
            logging.info('Admin account: "unclepat" already exists.')

    app.run() #debug=TRUE if want to debug
