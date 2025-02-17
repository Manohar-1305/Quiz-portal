import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallbacksecretkey')

    # Read database credentials from environment variables
    DB_USER = os.getenv('DB_USER', 'quiz_user')
    DB_PASSWORD = quote_plus(os.getenv('DB_PASSWORD', 'password'))  # Encodes special chars
    DB_HOST = os.getenv('DB_HOST', 'db')  # Use service name in Docker Compose
    DB_NAME = os.getenv('DB_NAME', 'quiz_db')

    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
