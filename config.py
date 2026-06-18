import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key-shop-insight'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shopvision.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
