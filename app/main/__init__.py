from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from ..config import app_config
from .routes.user import user
from .routes.blog import blog
from .routes.comments import comments

def create_app(environ):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[environ])
    app.config.from_pyfile("config.py")
    db.init_app(app)
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(blog, url_prefix="/blog")
    app.register_blueprint(comments, url_prefix="/comment")


    
    #@app.route("/hello/<username>")
    #def hello(username):
        #return "hello user {}".format(username)

    return app

