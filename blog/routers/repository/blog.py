from sqlalchemy.orm import Session
from blog import models
from fastapi import HTTPException,status


def get_all(db):
    blogs=db.query(models.Blog).all()
    return blogs


def blog_view(blog,db):
    new_blog=models.Blog(title=blog.title,body=blog.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show_blog(id,db):
    data=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    # response.status_code=status.HTTP_404_NOT_FOUND
    # return {"details":f"blog with the {id} is not availbale""}
    return data


def delete_blog_data(db,id):
    blog_data=db.query(models.Blog).filter(models.Blog.id==id).first()

    if not blog_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'blog id {id} not found')
    db.delete(blog_data)
    db.commit()
    return "Deleted"



def update_specific_blog(request,db,id):
    blog_data = request.model_dump(exclude_unset=True)
    print(f'blog data is{blog_data}')
    if 'body' in blog_data:
        blog_data['body'] = blog_data.pop('body')
    
    blog_val=db.query(models.Blog).filter(models.Blog.id==id)
    print(f"blog_post_new values:{blog_val} and id is:{id}")
    if not blog_val.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'blog id {id} not found')

    blog_val.update(blog_data)
    db.commit()
    return 'Updated'
