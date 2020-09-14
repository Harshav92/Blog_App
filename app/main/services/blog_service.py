from ..models.BlogModel import BlogModel, db 
from ..services.user_service import user_name, user_id


def add_blog(blog_name, description , author_id, content):
    try:
        blog = BlogModel(name=blog_name , descripition=description,author_id=author_id,content=content)
        db.session.add(blog)
        db.session.commit()
        return True
    except Exception as e:
        return e

def show_email(email):
    obj = user_id(email)
    if obj == None:
        return "user does not exist"
    else:
        ls = []
        blogs = BlogModel.query.filter_by(author_id=obj).all()
        for each in blogs:
            row = {}
            row['id'] = each.id
            row['name'] = each.name
            ls.append(row)
        return {"data":ls}



def show_blog():
    try:
        blogs = BlogContent.query.all()
        ls= []
        for each in blogs:
            blog = BlogModel.query.filter_by(id=each.blog_id).first()
            row = {}
            row["id"] = blog.id  
            row["description"] = blog.descripition
            row['name'] = blog.name
            row['author_name'] = user_name(blog.author_id)
            ls.append(row)
        return {"data":ls}
    except Exception as e:
        return e

def show_user(user_id):
    try:
        blogs = BlogModel.query.filter_by(user_id=user_id).all()
        ls = []
        for each in blogs:
            row = {}
            row["id"] = each.id
            row["description"] = each.descripition
            row['name'] = each.name
            ls.append(row)
        return {"data": ls}
    except Exception as e:
        return e

def delete_blog(blog_id, author_id):

    blogs = BlogModel.query.filter_by(id=blog_id).first()
    if blogs == None:
        return "blog does not exist"
    elif blogs.author_id !=author_id:
        return "User can not delete blog"
    elif blogs.author_id == author_id:
        db.session.delete(blogs)
        db.session.commit()
        return "blog deleted"


def update_blog(blog_id, content,user_id):
    blog = BlogModel.query.filter_by(id=blog_id).first()
    if blog == None:
        return "blog does not exist"
    elif blog.author_id != user_id:
        return "User can not edit blog"
    elif blog.author_id == user_id:
        blog.content=content  
        db.session.commit()
    


