from flask import Blueprint
from flask import request
from ..services.comment_service import *
import json


comments = Blueprint("comments", __name__)

@comments.route('/add', methods = ["POST"])
def add():
    result = add_comment(request.json['comment'], request.json['user_id'], request.json['blog_id'])
    return json.dumps({"msg":str(result)})

@comments.route('/show', methods= ['GET'])
def show():
    result = show_comments(request.json['blog_id'])
    return json.dumps({"msg": str(result)})


@comments.route('/list', methods=['GET'])
def drop():
    result = list_comment(request.json['blog_id'])
    return json.dumps({"msg":str(result)})

@comments.route('/subcomment', methods=['POST'])
def comment():
    result = comment_comment(request.json["comment_id"],request.json['user_id'], request.json["comment"])
    return json.dumps({"msg":str(result)})

@comments.route("/delete", methods=['delete'])
def delete():
    result = comment_delete(request.json['comment_id'],request.json['user_id'])
    return json.dumps({"msg":str(result)})

