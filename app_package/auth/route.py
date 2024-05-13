from flask import render_template, flash, redirect, url_for, request
from flask import request
from urllib.parse import urlsplit 
from app_package import app
from app_package.auth.forms import LoginForm
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from app_package import db
from app_package.models import User
from app_package.auth.forms import ResetPasswordRequestForm
from app_package.auth.email import send_password_reset_email
from app_package.auth.forms import ResetPasswordRequestForm, ResetPasswordForm
from flask_babel import gettext as _

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
      return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
      user = db.session.scalar(
          sa.select(User).where(User.username == form.username.data))
      if user is None or not user.check_password(form.password.data):
          flash(_('Invalid username or password'))
          return redirect(url_for('login'))
      login_user(user, remember=form.remember_me.data)
      next_page = request.args.get('next')
      if not next_page or urlsplit(next_page).netloc != '':
        next_page = url_for('index')
      return redirect(next_page)
    return render_template('login.html',  title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_('Congratulations, you are now a registered user!'))
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.email == form.email.data))
        if user:
            send_password_reset_email(user)
        flash(_('Check your email for the instructions to reset your password'))
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)  

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash(_('Your password has been reset.'))
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)