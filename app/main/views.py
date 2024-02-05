from . import main
from flask import render_template
from ..models import User


@main.route('/')
def index():
    return render_template("home.html")


@main.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

