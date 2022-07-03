from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, current_user
from ..service.forms import SignupForm, LoginForm
from .. import login_manager
from ..service import auth
from ..model.user import User

# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    static_folder='static'
)

# Get HTMLs for every page


@auth_bp.route('/', methods=["GET", "POST"])
def login():
    form = LoginForm()

    redirect_url = auth.login(current_user, request, form)

    if redirect_url:
        return redirect(url_for(redirect_url))

    # GET: Serve page
    return render_template(
        "index.html",
        form=form,
        template="form-template"
    )


@auth_bp.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()

    redirect_url = auth.signup(request, form)

    if redirect_url:
        return redirect(url_for(redirect_url))

    # GET: Serve page
    return render_template(
        "signup.html",
        form=form,
        template="form-template"
    )


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))


@login_manager.user_loader
def load_user(user_id):
    # Check if user is logged in
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    # Redirect unauthorized users
    flash('You must be logged in to view that page.')

    return redirect(url_for('auth_bp.login'))
