from flask import Flask,session, render_template,request,url_for, redirect 
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager,login_user
from flask_session import Session
import openai


app= Flask(__name__)
app.config["SECRET_KEY"] ="AtigyiUS9812892024IKOSNJSGDU"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    password= db.Column(db.String(50),nullable=False)
    username = db.Column(db.String(40),nullable=False)
    hash = db.Column(db.String(40),nullable=False)
    sppassword = db.Column(db.String, nullable= False)

db.init_app(app)
with app.app_context():
    db.create_all()

@login_manager.user_loader
def user_load(user_id):
   return Users.query.get(user_id)


@app.route('/')
def home():
    return render_template('/templates/index.html')
