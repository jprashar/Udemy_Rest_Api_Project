from app import app
from db import db

# This callback can be used to initialize an application for the use with this database setup.
db.init_app(app)

#To create all tables before first request 
@app.before_first_request
def create_tables():
    db.create_all()

