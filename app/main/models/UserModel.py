from ..import db
import datetime
from .import BlogModel
from .import CommentModel

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True , nullable=False)
    password = db.Column(db.String(15),nullable=False)
    db.UniqueConstraint("email")
    
