from . import main
from flask import render_template, flash
from ..models import User
from .. import db


@main.route('/')
def index():
    return render_template("home.html")


@main.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)



