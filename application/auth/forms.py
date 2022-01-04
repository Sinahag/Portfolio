from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.auth.models import User
from application import db


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me?")
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=100)])
    password_confirm = PasswordField("Confirm Password",
                                     validators=[DataRequired(), Length(min=6, max=100), EqualTo('password')])
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")
