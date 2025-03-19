from fastapi import APIRouter,Depends,HTTPException,status
from blog.database import get_db
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog import models,schemas
from blog.routers.repository.user import new_user_registration,get_specific_user_id


router=APIRouter(prefix='/user',
                 tags=['Users'])


@router.post('/',response_model=schemas.UserShow)
def create_user(request:schemas.User,db: Session = Depends(get_db)):
    return new_user_registration(db,request)


@router.get('/{id}',response_model=schemas.UserShow)
def get_user(id:int,db: Session = Depends(get_db)):
    return get_specific_user_id(id,db)