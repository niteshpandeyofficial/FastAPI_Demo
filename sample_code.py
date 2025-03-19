#its sample code hence include complete details in one file

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

@app.get('/')
def index():
    return 'Main Page'


class Blog(BaseModel):
    title: str
    body: str
    published: bool




@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f"Blog is created with title {blog.title}"}

@app.get('/blog')
def blog_post(limit=10,published:bool =True,sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published blog are present'}
    else:
        return {'data':f'{limit} blog are unpublished'}

@app.get('/blog/unpublished')
def unpublished_blog():
    return "This are the unpublished blog"

@app.get('/blog/{id}')
def blog_details(id:int):
    return {'data':id}

#if we use this path after above then it give error because it treat as the above path instead of this
# @app.get('/blog/unpublished')
# def unpublished_blog():
#     return "This are the unpublished blog"

@app.get('/about')
def about_page():
    return 'About page'


if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=9000)


