from fastapi import APIRouter,Depends,HTTPException,status
from blog import schemas,models,hashing
from blog.database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from blog.token import create_access_token

router=APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request:OAuth2PasswordRequestForm =Depends(),db:Session =Depends(get_db)):
    user =db.query(models.User).filter(models.User.email==request.username).first()
    print(f"user name is:{user}")
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid credential")
    
    if not hashing.Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect password")
    
    access_token=create_access_token(data={"sub":user.email})
    return {"access_token":access_token,"token_type":"bearer"}