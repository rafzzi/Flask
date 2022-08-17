import os

SECRET_KEY = 'afiga'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'password',
        servidor = 'localhost',
        database = 'jogoteca'
    )
    
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'