from flask import Blueprint
from flask import request
from ..services.blog_service import *
import json


blog = Blueprint("blog", __name__)

@blog.route("/create", methods=["POST"])
def add():
    result = add_blog(request.json["name"],request.json["description"],request.json['author_id'],request.json['content'])
    return json.dumps({"msg": str(result)})

@blog.route("/list", methods= ["GET"])
def show():
    result = show_blog()
    return json.dumps({"msg": str(result)})

@blog.route("/list/<email>", methods = ['GET'])
def show_user(email):
    result = show_email(email)
    return json.dumps({"msg": str(result)})

@blog.route("/delete", methods = ['DELETE'])
def remove():
    result =  delete_blog(request.json['blog_id'],request.json["author_id"])
    return json.dumps({"msg": str(result)})

@blog.route("/update", methods = ['POST'])
def update():
    result = update_blog(request.json['blog_id'],request.json['content'],request.json['user_id'])
    return json.dumps({"msg": str(result)})





