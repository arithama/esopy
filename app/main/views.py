from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import main
from .forms import EditProfileForm
from .. import db
from ..models import User


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

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


