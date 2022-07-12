
import csv
import json
from datetime import datetime
from os.path import exists
from pickle import EMPTY_DICT, EMPTY_LIST
import uuid

class employee:
    
    def __init__(self):
       self.InitCSV()
       self.InitJSON()

    @classmethod
    def InitCSV(self):
        filePath='data/employees.csv'
        fields=['id','name','fathername','designation','station','BPS','CurrentBPS','DOB','DOA','Remarks','created_at','updated_at']
        file_exists = exists(filePath)
        if file_exists:
            return
        else:
            file=open(filePath, 'w+')
            file.write('Employees')
            file.close()
            with open(filePath, 'w') as f:
                writer=csv.writer(f)
                writer.writerow(fields)
    @classmethod
    def InitJSON(self):
        filePath='data/employees.json'
        file_exists = exists(filePath)
        if file_exists:
            return
        else:
            obj={'employee':[]}
            with open(filePath, 'w',encoding='utf-8') as fwrite:    
                json.dump(obj,fwrite)
    @classmethod
    def CreateCSV(self,name:str,fathername:str,designation:str,station:str,BPS:str,CurrentBPS:str,DOB:str,DOA:str,Remarks:str):
        id=uuid.uuid4()
        datarow=[id,name,fathername,designation,station,BPS,CurrentBPS,DOB,DOA,Remarks,datetime.now(),datetime.now()]
        
        with open('data/employees.csv', 'a', encoding='UTF8') as f:
            writer=csv.writer(f)
            writer.writerow(datarow)
        return id
    @classmethod
    def GetCSV(self):
        header=[]
        rows=[]
        All=[]
        file=open('data/employees.csv')
        reader=csv.reader(file)
        header=next(reader)

        for row in reader:
            rows.append(row)
        file.close()
        rows=[ele for ele in rows if ele != []]
        All.append(header)
        All.append(rows)

        return All
    @classmethod
    def CreateJSON(self,name:str,fathername:str,designation:str,station:str,BPS:str,CurrentBPS:str,DOB:str,DOA:str,DOE:dict,Remarks:str):
        key="employee"
        filePath="data/"+key+"sdict.json"
        id=uuid.uuid4()
        now=datetime.now()
        datarow={"Id":str(id),"Name":name,"FatherName":fathername,"Designation":designation,"Station":station,"BPS":BPS,"CurrentBPS":CurrentBPS,"DOB":DOB,"DOA":DOA,"DOE":DOE,"Remarks":Remarks,"CreatedAt":now.strftime("%m/%d/%Y, %H:%M:%S"),"UpdatedAt":""}
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

    @classmethod
    def GetJSON(self):
        arr=[]
        with open('data/employeesdict.json', 'r',encoding='utf-8') as fread:
            data=json.load(fread)
            oldData=dict(data)
            arr=list(oldData.get("employee"))
        return arr

    @classmethod
    def UpdateEmpList(self,id:str,empList:list,editItems:dict):
        index=self.FindIndexWithKey("Id",id,empList)
        emp=empList[index]
        emp.update(editItems)
        empList.pop(index)#remove old Employee from list
        empList.append(emp)#append update employee in list
        self.UpdateJSON(empList)
       
    @classmethod
    def UpdateJSON(self,updatedEmpList:list):
        newData={'employee':updatedEmpList}
        with open('data/employeesdict.json', 'w',encoding='utf-8') as fwrite:    
           json.dump(newData,fwrite)

    @classmethod
    def FindWithKey(self,key,val,emplist:list):
        emp=next((d for d in emplist if d.get(key) == val), None)
        return emp #return dictionary type

    @classmethod
    def FindIndexWithKey(self,key,val,empList:list):
        index=next((index for (index, d) in enumerate(empList) if d.get(key) == val), None)
        return index

    # @classmethod
    # def GetDOE(self,id,list):
    #     empList=[]
    #     if list == EMPTY_LIST:
    #         empList=self.GetJSON()
    #     else:
    #         empList=list
    #     key="Id"
    #     val=id
    #     emp=next((d for d in empList if d.get(key) == val), None)
    #     DOEList= emp.get("DOE")
    #     return DOEList #return type will be of list of dictionary
    

    @classmethod
    def StrDateNow(self):
        now=datetime.now()
        return now.strftime("%m/%d/%Y, %H:%M:%S")
    @classmethod
    def TotalEmpCount(self):
        empList=self.GetJSON()
        return len(empList)