import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "0GcTBsB7OMjwUUvrr6XWU5us3NLYon5j"
    CSRF_ENABLED     = True
    CSRF_SESSION_KEY = "secret"
    MONGODB_SETTINGS = { 'db' : 'portfolio' , 
    'host' : 'mongodb+srv://portfolio.vrd4w.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority' } 

    
