from fastapi import FastAPI
from blog.database import engine
import uvicorn
from blog import models
from blog.routers import user,blog,login
app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)









    
    

