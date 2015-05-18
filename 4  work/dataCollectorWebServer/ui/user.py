from wtforms import StringField, validators

from lib.utils import WTForm

class LoginForm(WTForm):
    email = StringField('email', [
        validators.DataRequired(message = "A email is required."),
        validators.Length(min = 4, message = "Email length is wrong."),
        validators.Email(message = "Email Address is invalid.")
    ])

    password = StringField('password', [
        validators.DataRequired(message = "Password is required."),
        validators.length(min = 6, max = 64, message = "length of password between 6 and 64.")
    ])
