from flask import Blueprint
from flask import request
from ..services.user_service import *
import json

user = Blueprint("user",__name__)

@user.route("/register" , methods = ["POST"])
def add():
    result = add_user(request.json["name"],request.json["email"],request.json["password"])
    return json.dumps({"msg": str(result)})

    

@user.route("/login", methods = ['GET'])
def login():
    result = login_user(request.json["email"],request.json['password'])
    return json.dumps({"msg": str(result)})
