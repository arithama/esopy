from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm, PostForm
from .. import db
from ..models import User, Post


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.is_authenticated and form.validate_on_submit():
        post = Post(body=form.body.data,
        author=current_user._get_current_object(),
        title=form.title.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('home.html', form=form, posts=posts)


@main.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, posts=posts)
    

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

@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_profile_admin(id):
    if current_user.is_admin:
        user = User.query.get_or_404(id)
        form = EditProfileAdminForm(user=user)
        if form.validate_on_submit():
            user.email = form.email.data
            user.username = form.username.data
            user.confirmed = form.confirmed.data
            user.name = form.name.data
            user.about_me = form.about_me.data
            db.session.add(user)
            db.session.commit()
            flash('The profile has been updated.')
            return redirect(url_for('.user', username=user.username))
        form.email.data = user.email
        form.username.data = user.username
        form.confirmed.data = user.confirmed
        form.name.data = user.name
        form.about_me.data = user.about_me
        return render_template('edit_profile.html', form=form, user=user)
    else:
        return('You are not allowed to access this page')

@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)

    return render_template('post.html', post=post)