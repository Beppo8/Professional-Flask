class Config:
    SECRET_KEY = 'codigofacilito'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://beppo88:ewad8dis@localhost/flask_profesional'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}