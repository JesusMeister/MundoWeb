from sqlalchemy.orm import Session
import sqlalchemy

from model import postmodel
from schema import postschema

def create_post(db: Session, post: postschema.Post):
    db_post = postmodel.Post(
        id=None,
        title=post.title,
        content=post.content,
        project=post.project,
        startDate=post.startDate,
        endDate=post.endDate,
        hoursPerDay=post.hoursPerDay,
        status=post.status,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def list_posts(db: Session):
    posts = db.query(postmodel.Post).all()
    posts = sorted(posts, key=lambda x: x.project)
    return posts

def list_projects(db: Session):
    projects = db.query(postmodel.Post.project).group_by(postmodel.Post.project).all()
    return projects

def find_by_project(db: Session, project: str):
    posts = db.query(postmodel.Post).filter(postmodel.Post.project == project).all()
    return posts


def delete_project(db: Session, project: str):
    posts = db.query(postmodel.Post).filter(postmodel.Post.project == project).all()
    for post in posts:
        db.delete(post)
    db.commit()
    return posts

def delete_task(db: Session, id: int):
    post = db.query(postmodel.Post).filter(postmodel.Post.id == id).first()
    db.delete(post)
    db.commit()
    return post

def change_status(db: Session, title: str):
    post = db.query(postmodel.Post).filter(postmodel.Post.title == title).first()
    if post:
        post.status = True
    db.commit()
    db.refresh(post)
    return post

def update_task(db: Session, post: postschema.Post):
    db_post = db.query(postmodel.Post).filter(postmodel.Post.id == post.id).first()
    if db_post:
        db_post.title=post.title
        db_post.content=post.content
        db_post.project=post.project
        db_post.startDate=post.startDate
        db_post.endDate=post.endDate
        db_post.hoursPerDay=post.hoursPerDay
        db_post.status=post.status
    db.commit()
    db.refresh(db_post)
    return db_post

def find_by_id(db: Session, id: int):
    post = db.query(postmodel.Post).filter(postmodel.Post.id == id).first()
    return post