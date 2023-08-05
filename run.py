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
from app import app, store 
from app.models import User

# ========================================================================================================
# RUN FLASK APP
# ========================================================================================================
if __name__ == '__main__':
    with app.app_context():
        store.create_all()

        # if admin user dont exist, create it
        new_user = User('chydarren', 'test')

        # check if user exists
        user = User.query.filter_by(username='chydarren').first()

        if user is None:
            store.session.add(new_user)
            store.session.commit()
            
    app.run(debug=True)
