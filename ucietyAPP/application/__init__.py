#Importation of relevant modules needed

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
#the secret key is needed to keep the client-side session secure
app.config['SECRET_KEY'] = '6732vbu3d3237bdjbkwqebd239739323'
####
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
'''The login manager contains the code that lets your application
and Flask-login work together'''
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
