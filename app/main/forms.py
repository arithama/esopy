from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import InputRequired, Length, Email, Regexp, DataRequired
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import User

class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        InputRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    name = StringField('Real name', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
        
class PostForm(FlaskForm):
    title = TextAreaField("What is the title of your story?", validators = [DataRequired()])
    body = PageDownField("What story do you want to tell?", validators=[DataRequired()])
    submit = SubmitField('Submit')