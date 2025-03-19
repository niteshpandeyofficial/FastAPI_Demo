from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from typing import List
from blog import models, schemas
from blog.database import get_db
from blog.routers.repository.blog import get_all,blog_view,show_blog,delete_blog_data,update_specific_blog
from blog.routers.OAuth2Password import get_current_user

router=APIRouter(
    prefix='/blog',
    tags=['Blogs']
                 )


@router.get('/',response_model=List[schemas.ShowBlog])
def get_blog_details(db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return get_all(db)


#Add the blog
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(blog:schemas.Blog,db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return blog_view(blog,db)

#fetch the specific blog based on Id
@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def display(id:int,response:Response,db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return show_blog(id,db)


#delete blog 
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    result=delete_blog_data(db,id)
    print(f"result is {result}")
    return result
    

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int,request:schemas.Blog,db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return update_specific_blog(request,db,id)




# #fetch the blog details
# @app.get('/blog',response_model=List[schemas.ShowBlog])
# def get_blog_details(db: Session = Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs


# @app.get('/blog/{id}',status_code=status.HTTP_404_NOT_FOUND)
# def display(id,db: Session = Depends(get_db)):
#     data=db.query(models.Blog).filter(models.Blog.id==id).first()
#     return data


