from flask import Blueprint, render_template, request, make_response, redirect, url_for
from flask_login import login_required
from ..model import user
User = user.User

# Blueprint Configuration
routes_bp = Blueprint(
    'routes_bp', __name__,
    static_folder='static'
)


@routes_bp.route('/linktree', methods=["GET", "POST"])
@login_required
def linktree():
    return render_template('linktree.html')


@routes_bp.route('/gore', methods=["GET"])
@login_required
def gore():
    return render_template('gore.html')
