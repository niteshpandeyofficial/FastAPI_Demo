from blog import models
from blog.hashing import Hash
from fastapi import HTTPException,status

def new_user_registration(db,request):
        new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user


def get_specific_user_id(id,db):
            user=db.query(models.User).filter(models.User.id==id).first()
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User id {id} not found")
            return user