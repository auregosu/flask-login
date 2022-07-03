from flask import flash, Request
from flask_login import login_user
from .forms import SignupForm, LoginForm
from ..model.user import User
from .. import db

def login(current_user, request: Request, form: LoginForm):
    if current_user.is_authenticated:
        return 'routes_bp.linktree'

    # POST: Log user in
    if request.method == 'POST':

        if form.username.data != "" and form.password.data != "":
            check_user = User.query.filter_by(name=form.username.data).first()

            if check_user and check_user.check_password(password=form.password.data):
                login_user(check_user)

                return 'routes_bp.linktree'

        flash('Invalid username/password combination.')

        return 'auth_bp.login'

def signup(request: Request, form: SignupForm):
    # POST: Sign user in
    if request.method == 'POST':

        if form.username.data != "" and form.email.data != "" and form.password.data != "":
            existing_user = User.query.filter(User.name == form.username.data).first()

            if existing_user is None:
                new_user = User(
                    name=form.username.data,
                    email=form.email.data,
                )
                new_user.set_password(form.password.data)
                db.session.add(new_user)
                db.session.commit()

                return 'auth_bp.login'

            flash('That name is already registered.')
