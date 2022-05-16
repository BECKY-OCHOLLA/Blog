
from flask import render_template,request,redirect,url_for,abort
from app.requests import get_quote
from app.main import main
# from models import Quote
from flask_login import login_required
from ..models import Reviews, User
from .forms import ReviewForm,UpdateProfile
from .. import db


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    Quote = get_quote()
   
    title = 'Bekitas Blog'
    return render_template('index.html',  title = title, Quote=Quote)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)