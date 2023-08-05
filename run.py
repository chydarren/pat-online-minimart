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
        # if admin user dont exist, create it
        new_user = User('chydarren', 'test')

        # check if user exists
        user = User.query.filter_by(username='chydarren').first()

        if user is None:
            storeDb.session.add(new_user)
            storeDb.session.commit()

        storeDb.create_all()
            
    app.run(debug=True)
