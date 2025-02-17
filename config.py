import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:15haziran@localhost:3306/newproje'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

