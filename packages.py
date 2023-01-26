# def add(a,b):
#     return(a+b)
# def add_n_numbers(*arr):
#     return sum(arr)




#PROGRAM 4 PACKAGES

from CRTDAY4 import User

class Login:
    __db=[]
    def create_user(self,full_name,email,password):
        new_user=User(full_name,email,password)
        self.__db.append(new_user)
    def validate_user(self,email,password):
        pass
obj