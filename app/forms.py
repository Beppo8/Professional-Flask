import email_validator
from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField

from .models import User

def codi_validator(form, field):
    if field.data == 'codi' or field.data == 'Codi':
        raise validators.ValidationError('El username codi no es permitido')

class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='El username se encuentra fuera de rango')
    ])
    password = PasswordField('Password', [
        validators.Required(message='El email es requerido')
    ])

class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50),
        codi_validator
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100),
        validators.Required(message='El email es requerido'),
        validators.Email(message='Ingrese un email valido')
    ])
    password = PasswordField('Password', [
        validators.Required('El password es requerido.'),
        validators.EqualTo('confirm_password', message='La contraseña no coincide')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('', [
        validators.DataRequired()
    ])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El username ya se encuentra en uso')
    
    def validate_email(self, email):
        if User.get_by_email(username.data):
            raise validators.ValidationError('El username ya se encuentra en uso')

    def validate(self):
        if not Form.validate(self):
            return False

        if len(self.password.data) < 3:
            self.password.errors.append('El password el demasiado corto')
            return False

        return True
