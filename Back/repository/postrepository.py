from sqlalchemy.orm import Session

from model import postmodel
from schema import postschema

def create_post(db: Session, post: postschema.Post):
    db_post = postmodel.Post(title=post.title,content=post.content,project=post.project,
                             startDate=post.startDate,endDate=post.endDate,
                             hoursPerDay=post.hoursPerDay, status=post.status)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def list_posts(db:Session):
    posts = db.query(postmodel.Post).all()
    posts = sorted(posts, key=lambda x: x.project)
    return posts

def find_by_project(db:Session, project:str):
    posts = db.query(postmodel.Post).filter(postmodel.Post.project==project).all()
    return posts

def delete_project(db:Session, project:str):
    posts = db.query(postmodel.Post).filter(postmodel.Post.project==project).all()
    for post in posts:
        db.delete(post)
    db.commit()
    return posts

def change_status(db:Session, title:str):
    post = db.query(postmodel.Post).filter(postmodel.Post.title==title).first()
    if post:
        post.status = True
    db.commit()
    db.refresh(post)
    return post