
from flask import render_template,request,redirect,url_for
from app.requests import get_quote
from app.main import main
# from models import Quote
from flask_login import login_required

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    Quote = get_quote()
   
    title = 'Bekitas Blog'
    return render_template('index.html',  title = title, Quote=Quote)