import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4


db = SQLAlchemy()
app = Flask(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/expenzo"

db.init_app(app)

from .expense import expense
from .user import user
app.register_blueprint(expense)
app.register_blueprint(user)