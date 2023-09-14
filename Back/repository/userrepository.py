from sqlalchemy.orm import Session

from model import usermodel
from schema import userschema

def create_user(db: Session, user: userschema.User):
    db_user = usermodel.User(email=user.email,name=user.name,last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def list_users(db:Session):
    users= db.query(usermodel.User).all()
    return users

def find_by_id(db:Session, id:int):
    user=db.query(usermodel.User).filter(usermodel.User.id==id).first()
    return user