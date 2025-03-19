from passlib.context import CryptContext
import bcrypt

pwd_ext=CryptContext(schemes=["bcrypt"],deprecated="auto")
class Hash:
    def bcrypt(password:str):
        pwd_encrypt=pwd_ext.hash(password)
        return pwd_encrypt
    

    def verify(db_password,user_password):
        return pwd_ext.verify(user_password,db_password)
        