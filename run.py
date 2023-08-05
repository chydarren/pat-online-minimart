'''
Author: Chua Han Yong Darren
Date: 04/08/2023 
Application: Pat's Online Minimart
File: run.py
'''
# ========================================================================================================
# IMPORTS AND CONFIGURATIONS
# ========================================================================================================
# Import instances
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
            storeDb.session.add(User('unclepat', 'unclepat_2023_08'))
            storeDb.session.commit()

    app.run() #debug=TRUE if want to debug
