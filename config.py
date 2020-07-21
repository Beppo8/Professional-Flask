from decouple import config

class Config:
    SECRET_KEY = 'codigofacilito'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://beppo88:ewad8dis@localhost/flask_profesional'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

<<<<<<< HEAD
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://beppo88:ewad8dis@localhost/flask_profesional_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True
=======
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'beppo2488@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')
>>>>>>> email

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}