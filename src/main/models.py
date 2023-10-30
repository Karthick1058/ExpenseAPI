from flask_sqlalchemy import SQLAlchemy
from main import db
import json


class Expense(db.Model):
    __tablename__ = 'expense'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)


class ExpenseCategory(db.Model):
    __tablename__ = 'expense_category'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, nullable=False)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    accessToken = db.Column(db.String, nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    