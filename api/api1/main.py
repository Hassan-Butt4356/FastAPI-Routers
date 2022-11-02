from fastapi import APIRouter

from .schemas import CreateUser,UpdateUser

router=APIRouter(
    prefix='/api1'
)

@router.get('/home',tags=['API1'])
def home():
    return {'Response':'This is Home From API1'}


users=[]

@router.post('/create_user',response_model=CreateUser,tags=['API1'])
def createUser(user:CreateUser):
    new_user={'name':user.name,'email':user.email,'age':user.age}
    users.append(new_user)
    return new_user

@router.get('/get_users',tags=['API1'])
def getUsers():
    if users:
        return users
    else:
        return {"Response":'No user is added'}

@router.get('/get_user',tags=['API1'])
def getUser(name:str):
    for user in users:
        if user['name']==name:
            return user
    return {'Response':'User Not Found'}

@router.put('/update_user',response_model=UpdateUser,tags=['API1'])
def getUser(name:str,user:UpdateUser):
    for update_user in users:
        if update_user['name']==name:
            update_user['name']=user.name
            update_user['email']=user.email
            update_user['age']=user.age
            return update_user
    return {'Response':'User Not Found'}


@router.delete('/delete_user',tags=['API1'])
def deleteUser(name:str):
    for user in users:
        if user['name']==name:
            users.remove(user)
            return {'Response':'User Deleted SuccessFully'}
    return {'Response':'User Not Found'}