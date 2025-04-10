from models.User import User
from config import db

def get_all_user():
    return [user.to_dict() for user in User.query.all()]

def get_user_by_id(user_id):
    user = User.query.get_or_404(user_id)
    return user.to_dict()

def create_user(data):
    new_user = User(name=data.get('name'), email=data.get('email'))
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()

def update_user(user_id, data):
    user = User.query.get_or_404(user_id)
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return user.to_dict()

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {"message": "User deleted successfully"}
