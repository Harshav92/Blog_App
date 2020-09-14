from ..models.UserModel import UserModel , db  



def add_user(name, email, password):
    try:
        user = UserModel( name=name, email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return "user added"
    except Exception as e:
        return str(e)

def user_name(id):
    user = UserModel.query.filter_by(id=id).first()
    return user.name

def login_user(email, password):
    try:
        user = UserModel.query.filter_by(email=email).first()
        if user == None:
            return "user does not exist please register"
        elif user.password == password:
            
            return "login succesfull"
        else:
            return "user details do not match"
    except Exception as e:
        return str(e)

def user_id(email):
    user_id = UserModel.query.filter_by(email=email).first()
    if user_id == None:
        return None
    else:
        return user_id.id
