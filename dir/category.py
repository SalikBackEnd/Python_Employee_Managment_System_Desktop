from os.path import exists
import json
import uuid
from datetime import datetime
class category:

    def __init__(self):
       self.InitJSON()
    @classmethod
    def InitJSON(self):
        filePath='data/category.json'
        file_exists = exists(filePath)
        if file_exists:
            return
        else:
            obj={'category':[]}
            with open(filePath, 'w',encoding='utf-8') as fwrite:    
                json.dump(obj,fwrite)
    @classmethod
    def CreateJSON(self,name:str):
        key="category"
        filePath="data/category.json"
        id=uuid.uuid4()
        now=datetime.now()
        datarow={"Id":str(id),"Name":name,"CreatedAt":now.strftime("%m/%d/%Y, %H:%M:%S"),"UpdatedAt":""}
       # jsondata=json.dumps(datarow, indent=4, sort_keys=True)
        newData={}
        with open(filePath, 'r',encoding='utf-8') as fread:
            data=json.load(fread)
            oldData=dict(data)
            arr=list(oldData.get(key))
            arr.append(datarow)
            newData={key:arr}
            print(newData)
        with open(filePath, 'w',encoding='utf-8') as fwrite:    
            json.dump(newData,fwrite)
        return id