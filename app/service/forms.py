from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
)
from wtforms.validators import DataRequired


class SignupForm(FlaskForm):
    # Sign up for a user account.
    username = StringField(
        'Username',
        [DataRequired()]
    )

    email = StringField(
        'Email',
        [DataRequired()]
    )

    password = PasswordField(
        'Password',
        [DataRequired(message="Please enter a password.")]
    )

    recaptcha = RecaptchaField()

    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    # Log in with an user
    username = StringField(
        'Username',
        validators=[DataRequired()]
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired(message="Please enter a password.")]
    )

    submit = SubmitField('Enter')
