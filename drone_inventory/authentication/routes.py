from flask import Blueprint, flash, render_template, request, redirect, url_for
from drone_inventory.forms import UserLoginForm
from drone_inventory.models import User, db, check_password_hash
from flask_login import login_user, login_required, logout_user

auth= Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods =['GET', 'POST'])
def signup():
  form = UserLoginForm()
  if request.method == "POST" and form.validate_on_submit():
    email = form.email.data
    password = form.password.data
    print([email, password])
    
    #creating a new user instance and adding that user to the user table
    user = User(email, password)
    db.session.add(user)
    db.session.commit()

    
    #flashed message for successful sign up
    flash(f'You have successfully created a user account {email}', 'user-created')
    #rederecting to home page
    return redirect(url_for('site.home'))
    
  return render_template('signup.html', form = form)


@auth.route('/signin', methods =['GET', 'POST'])
def signin():
  form = UserLoginForm()
  if request.method == 'POST' and form.validate_on_submit():
    email = form.email.data
    password = form.password.data
    print([email, password])
    
    logged_user = User.query.filter(User.email == email).first()
    if logged_user and check_password_hash(logged_user.password, password):
      login_user(logged_user)
      flash('You were successfully logged in.', 'auth-success')
      return redirect(url_for('site.home'))
    else:
      flash('Your Email/Password is incorrect', 'auth-failed')
      return redirect(url_for('auth.signin'))

      
  return render_template('signin.html', form = form)



@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('site.home'))
