from fastapi import FastAPI,Depends
from schema.userschema import User
from schema.postschema import Post
from repository import userrepository, postrepository
from database import SessionLocal, engine
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
@app.get("/")
async def hello_world():
    return {"message":"Hello World"}


@app.get("/hello/{name}")
async def hello_name(name:str):
    return {"message":f"Hello {name}"}


@app.post("/hello-post")
async def hello_name(user:User):
    return {"message":f"Hello {user.name}"}

@app.post("/user/create",response_model=User)
async def create_user(user:User, db: Session = Depends(get_db)):
    user=userrepository.create_user(db,user)
    return user

@app.get("/user/list",response_model=list[User])
async def list_users(db: Session = Depends(get_db)):
    users=userrepository.list_users(db)
    return users

@app.get("/user/find/{id}",response_model=User)
async def find_by_id(db:Session=Depends(get_db),id:int=0):
    print(id)
    user=userrepository.find_by_id(db,id)
    print(user)
    return user

@app.post("/post/create",response_model=Post)
async def create_post(post:Post, db: Session = Depends(get_db)):
    post=postrepository.create_post(db,post)
    return post

@app.get("/post/list",response_model=list[Post])
async def list_posts(db: Session = Depends(get_db)):
    posts=postrepository.list_posts(db)
    return posts

@app.get("/post/find-by-project/{project}",response_model=list[Post])
async def find_by_project(db:Session=Depends(get_db),project:str=""):
    print(project)
    post=postrepository.find_by_project(db,project)
    print(post)
    return post

@app.delete("/post/delete-by-project/{project}")
async def delete_by_project(db:Session=Depends(get_db),project:str=""):
    print(project)
    post=postrepository.delete_project(db,project)
    print(post)


@app.put("/post/change-status/{title}")
async def change_status(db:Session=Depends(get_db),title:str=""):
    print(title)
    post=postrepository.change_status(db,title)
    print(post)