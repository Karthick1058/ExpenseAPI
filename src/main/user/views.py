from main.models import db, User
from main import app
from flask import Flask, jsonify, request
from uuid import uuid4
import jwt
from . import user

@user.route('/user/create', methods=['POST'])
def sign_up():
    user = request.get_json()
    email = user["email"]
    password = user["password"]
    user = User(email=email, password=password, accessToken= uuid4())
    db.session.add(user)
    db.session.commit()
    return '', 201
        
@user.route('/user', methods=['POST'])
def sign_in():
    user = request.get_json()
    email = user["email"]
    password = user["password"]

    user = User.query.filter_by(email=email).first()
    if(user.password == password):
        token = jwt.encode({"email": email, "access_token": user.accessToken},app.config["SECRET_KEY"],algorithm="HS256")
        userJson = user.as_dict()
        userJson["token"] = token
        userJson.pop("accessToken")
        userJson.pop("password")
        userJson.pop("id")
        print(userJson["token"])
        return userJson, 200
        # return {
        #     "id": user.id,
        #     "email": user.email,
        #     "accessToken": user.accessToken
        # }, 200

    else:
        return "Password is not correct", 401
