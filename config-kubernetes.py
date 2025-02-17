import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallbacksecretkey')

    # Read database credentials from Kubernetes environment variables
    DB_USER = os.getenv('DB_USER', 'quiz_user')
    DB_PASSWORD = quote_plus(os.getenv('DB_PASSWORD', 'password'))  # Encodes special chars
    DB_HOST = os.getenv('DB_HOST', 'mysql-quiz-service')  # Use Kubernetes service name
    DB_NAME = os.getenv('DB_NAME', 'quizdb')

    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
