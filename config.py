import os

class Config:
    SECRET_KEY = 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'mysql://quiz_user:password@43.205.116.98/quiz_db'  # Ensure this is set before SQLAlchemy initialization
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optionally disable modification tracking
