from fastapi import FastAPI,Depends
from schema.userschema import User
from schema.postschema import Post, Project
from repository import userrepository, postrepository
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/post/create",response_model=Post)
async def create_post(post:Post, db: Session = Depends(get_db)):
    post=postrepository.create_post(db,post)
    return post

@app.get("/post/list",response_model=list[Post])
async def list_posts(db: Session = Depends(get_db)):
    posts=postrepository.list_posts(db)
    return posts

@app.get("/project/list", response_model=list[Project])
async def list_projects(db:Session=Depends(get_db)):
    projects=postrepository.list_projects(db)
    return projects

@app.get("/post/find-by-project/{project}",response_model=list[Post])
async def find_by_project(db:Session=Depends(get_db),project:str=""):
    print(project)
    post=postrepository.find_by_project(db,project)
    print(post)
    return post

@app.get("/post/find-by-id/{id}",response_model=Post)
async def find_by_id(db:Session=Depends(get_db),id:int=0):
    print(id)
    post=postrepository.find_by_id(db,id)
    print(post)
    return post

@app.delete("/post/delete-by-project/{project}")
async def delete_by_project(db:Session=Depends(get_db),project:str=""):
    print(project)
    post=postrepository.delete_project(db,project)
    print(post)

@app.delete("/post/delete/{id}")
async def delete_task(db:Session=Depends(get_db),id:int=0):
    print(id)
    post=postrepository.delete_task(db,id)
    print(post)


@app.put("/post/change-status/{title}")
async def change_status(db:Session=Depends(get_db),title:str=""):
    print(title)
    post=postrepository.change_status(db,title)
    print(post)

@app.post("/post/update/{id}",response_model=Post)
async def update_task(post: Post, db: Session=Depends(get_db)):
    post=postrepository.update_task(db, post)
    return post