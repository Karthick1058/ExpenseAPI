from main.auth_middleware import token_required
from main.models import db, Expense, ExpenseCategory
from flask import Flask, jsonify, request
from . import expense

@expense.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@expense.route('/expenses')
@token_required
def get_expenses(current_user):
    # expenses = db.session.execute(db.select(Expense).order_by(Expense.name)).scalars()
    expenses = Expense.query.filter_by(user_id=current_user.id).join(ExpenseCategory, Expense.category_id == ExpenseCategory.id).add_columns(Expense.name, Expense.description, Expense.amount, Expense.date, ExpenseCategory.category)
    print(expenses)
    expense_arr = []
    for row in expenses:
        data = {}
        data['name'] = row.name
        data['description'] = row.description
        data['amount'] = row.amount
        data['date'] = row.date
        data['category'] = row.category
        expense_arr.append(data)
    return expense_arr


@expense.route('/expense', methods=['POST'])
@token_required
def add_expense(current_user):
    expense = request.get_json()
    name = expense['name']
    description = expense['description']
    amount = expense['amount']
    date = expense['date']
    category = expense['category']

    expense_categories = fetch_categories()

    if(category not in expense_categories):
        category = "miscellaneous"

    expense = Expense(name= name, description= description, amount=amount, date=date, category_id=category_id(category), user_id=current_user.id)
    db.session.add(expense)
    db.session.commit()
    return '', 204


def fetch_categories():
    expense_categories = db.session.execute(db.select(ExpenseCategory)).scalars()
    expense_category_arr = []
    for row in expense_categories:
        expense_category_arr.append(row.category)
    return expense_category_arr

def category_id(cat):
    category = ExpenseCategory.query.filter_by(category=cat).first()
    return category.id
