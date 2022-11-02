from fastapi import APIRouter,BackgroundTasks
from .schemas import CreateItem,UpdateItem


router=APIRouter(
    prefix='/api2'
)


@router.get('/home',tags=['API2'])
def home( background_tasks: BackgroundTasks):
    def myfun():
        i=0
        while i<5:
            i+=1
            print(f"This is background Task {i}")
            
    background_tasks.add_task(myfun)
    background_tasks.add_task(myfun)

    return {'Response':'This is Home from API2 '}



items=[]

@router.post('/create_item',response_model=CreateItem,tags=['API2'])
def createUser(item:CreateItem):
    new_item={'name':item.name,'description':item.description,'price':item.price}
    items.append(new_item)
    return new_item

@router.get('/get_items',tags=['API2'])
def getUsers():
    if items:
        return items
    else:
        return {"Response":'No Item is added'}

@router.get('/get_item',tags=['API2'])
def getUser(name:str):
    for item in items:
        if item['name']==name:
            return item
    return {'Response':'Item Not Found'}

@router.put('/update_item',response_model=UpdateItem,tags=['API2'])
def getUser(name:str,item:UpdateItem):
    for update_item in items:
        if update_item['name']==name:
            update_item['name']=item.name
            update_item['description']=item.description
            update_item['price']=item.price
            return update_item
    return {'Response':'Item Not Found'}


@router.delete('/delete_iten',tags=['API2'])
def deleteUser(name:str):
    for item in items:
        if item['name']==name:
            items.remove(item)
            return {'Response':'item Deleted SuccessFully'}
    return {'Response':'User Not Found'}