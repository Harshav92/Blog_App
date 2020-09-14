from ..models.CommentModel import CommentModel, CommentTree, db
from .user_service import user_name


def add_comment(comment,user_id,blog_id):
    try:
        cmnt_list = CommentModel.query.all()
        ls = []
        for each in cmnt_list:
            ls.append(each.id)
        comment = CommentModel(comment=comment, user_id=user_id, blog_id=blog_id )
        db.session.add(comment)
        db.session.commit()
        new_list = CommentModel.query.all()
        new_id = None
        for each in new_list:
            if each.id not in ls:
                new_id = each.id  
                break
        ct = CommentTree(ancestor=new_id,
                         length=0, descendant=new_id)
        db.session.add(ct)
        db.session.commit()

        
        return True
    except Exception as e:
        return e

def comment_comment(comment_id,user_id,comments):
    cmnt_list = CommentModel.query.all()
    ls = []
    for each in cmnt_list:
        ls.append(each.id)
    comment = CommentModel.query.filter_by(id=comment_id).first()
    blog_id = comment.blog_id
    comment = CommentModel(comment=comments, user_id=user_id,blog_id=blog_id)
    db.session.add(comment)
    db.session.commit()
    new_cmnt = CommentModel.query.all()
    cmnt_id = None
    for each in new_cmnt:
        if each.id not in ls:
            cmnt_id = each.id
            break
    
     
    comment_tree = CommentTree.query.filter_by(descendant=comment_id).all()
    for each in comment_tree:
        ct = CommentTree(ancestor=each.ancestor,length=each.length+1,descendant=cmnt_id)
        db.session.add(ct)
        db.session.commit()

    ct = CommentTree(ancestor=cmnt_id,
                     length=0, descendant=cmnt_id)
    db.session.add(ct)
    db.session.commit()
    return True



def show_comments(blog_id):
    try:
        comments = CommentModel.query.filter_by(blog_id=blog_id).all()
        ls = []
        for each in comments:
            row = {}
            row["id"] = each.id
            row["comment"] = each.comment
            row['author_name'] = user_name(each.user_id)
            ls.append(row)
        return {"data": ls}
    except Exception as e:
        return e

def tree(comment_id,level):
    ct = CommentTree.query.filter_by(ancestor=comment_id,length=1).all()
        
    ls = []
    for each in ct:
        row = CommentModel.query.filter_by(id=each.descendant).first()
        string = "level_{} --> id : {} , comment : {} , author_name : {}".format(
            level,row.id, row.comment, user_name(row.user_id))
        ls.append({string:tree(each.descendant,level+1)})
    if len(ls)>0:
        return ls
    else:
        return "end"





def list_comment(blog_id):
    try:
        comments = CommentModel.query.filter_by(blog_id=blog_id).all()
        ls = []
        #cts = []
        for each in comments:
            #quer = "select count(*) from comment_tree where descendant = {} and length={}".format(each.id, 1)
            #counts = db.session.execute(quer).scalar()
            counts = db.session.query(CommentTree).filter_by(descendant=each.id,length=1).count()
            #cts.append(counts)
            
            if counts == 0:
                string = "level_0 --> id : {} , comment : {} , author_name : {}".format(
                    each.id,each.comment,user_name(each.user_id))
                ls.append({string:tree(each.id,1)})
                

        return {"comments": ls}
    except Exception as e:
        return e

def comment_delete(comment_id,user_id):
    comment = CommentModel.query.filter_by(id=comment_id).first()
    if user_id == comment.user_id:
        comm_desc = CommentTree.query.filter_by(ancestor=comment.id).all()
        
        for each in comm_desc:
            comm = CommentModel.query.filter_by(id=each.descendant).first()
            db.session.delete(comm)
            db.session.commit()
        return True
    else:
        return "user can not delete"


def edit_comment(comment_id, comment,user_id):
    comm = CommentModel.query.filter_by(id=comment_id).first()
    if comm == None:
        return "comment does not exist"
    elif comm.user_id != user_id:
        return "User can not edit comment"
    elif comm.user_id == user_id:
        comm.comment = comment
        db.session.commit()
            



   



