from flask import Flask,session, render_template,request,url_for, redirect 
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_session import Session
import requests
