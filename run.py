

from tkinter import *
from datetime import datetime




from gui_methods import guiMethod
from dir.helper import helper

#InsertedId=emp.Create("Salik Ahmed1","Shakeel Ahmed1","Clerk","Station 1","19","20","05-06-1985","01-01-2008","Not Availabe")
#all=emp.GetAll()
# DOE={"DOE":'02-03-2010',"CreatedAt":emp.StrDateNow()}
#InsertedId=emp.CreateJSON("Nabeel Khanjee","Shakeel Khanjee","Clerk","Station 4","19","20","05-06-1995","09-04-2018","23-02-2010","NA")
#print(InsertedId)

# List=emp.GetJSON()
# id="f428ffe0-010d-46f8-b4ff-cdd795a6dbcf"
# FindList=emp.FindWithKey("Id",id,List)
# emp.UpdateEmpList(id,List,{'Name':"Salik Khilji","DOB":"05-06-2000"})

#print(emp.FindIndexWithKey("Id",id,List))
# MainWindow=Tk()
# MainWindow.geometry("650x250")

# def popList():
#     guiMethod.PopulateList(MainWindow)

# x=Button(MainWindow,text ="Hello", command = popList)
# x.place(x = 100,y = 200)
# MainWindow.mainloop()
gui=guiMethod()

window=gui.window
canvas=gui.canvas
addEmpBtn=gui.addEmpBtn
