from flask import Blueprint, url_for, render_template, flash, request
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.utils import redirect
from application import db
from application.auth.models import User
from application.auth.forms import RegisterForm, LoginForm


auth = Blueprint('auth',__name__)

@auth.route("/login")
def login():
    form = LoginForm()
    return render_template('auth/login.html', title="Login", login=True, form=form)


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.objects(email=email).first()

    if not user or not user.get_password(password):
        flash('Invalid login details, please try again.', "error")
        return redirect(url_for('auth.login'))
    else:
        flash(f"{user.name}, you are successfully logged in!", "success")
        user.authenticated = True

    login_user(user, remember=remember)
    return redirect(url_for('main.projects'))


@auth.route("/register")
def register():
    form = RegisterForm()
    return render_template("auth/register.html", title="Register", form=form, register=True)

@auth.route("/register", methods=['POST'])
def register_post():
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('password_confirm')
    name = request.form.get('name')
    user = User.objects(email=email).first()

    if user:
        flash('Email address already exists', "error")
        return redirect(url_for("auth.login"))

    if password != confirm_password:
        flash('Passwords do not match', 'warning')
        return redirect(url_for("auth.register"))

    new_user = User(id=User.objects.count() + 1, email=email, name=name)
    new_user.set_password(password)
    new_user.save()
    return redirect(url_for('auth.login'))

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out, successfully', "success")
    return redirect(url_for('main.index'))
