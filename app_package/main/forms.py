from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired
import sqlalchemy as sa
from app_package import db
from app_package.models import User
from wtforms import TextAreaField
from wtforms.validators import Length
from flask_babel import lazy_gettext as _l
from flask import request, current_app

class EditProfileForm(FlaskForm):
  username = StringField(_l('Username'), validators=[DataRequired()])
  about_me = TextAreaField(_l('About me'), validators=[Length(min=0, max=140)])
  submit = SubmitField(_l('Submit'))

  def __init__(self, original_username, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.original_username = original_username

  def validate_username(self, username):
    if username.data != self.original_username:
        user = db.session.scalar(sa.select(User).where(User.username == self.username.data))
        if user is not None:
            current_app.logger.error(_l('Please use a different username.'))
            raise ValidationError(_l('Please use a different username.'))
        
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')    

class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))  

class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'meta' not in kwargs:
            kwargs['meta'] = {'csrf': False}
        super(SearchForm, self).__init__(*args, **kwargs)      