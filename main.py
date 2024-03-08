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
