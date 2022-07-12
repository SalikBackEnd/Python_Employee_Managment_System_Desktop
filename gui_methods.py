

from ctypes.wintypes import BOOLEAN
from datetime import date
import os
import sys
from tkinter import ttk

from dir.employee import employee
from dir.helper import helper
from pathlib import Path
from tkcalendar import DateEntry
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from tkinter import messagebox
class guiMethod:
    emp=employee()
    window=Tk()
    canvas=Canvas()
    addEmpBtn=Button()
    showEmpBtn=Button()
    EmpTable=ttk.Treeview()
    MainFrame=Frame(window,background="Black")

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    @classmethod
    def resource_path(self,relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self) -> None:
                       
        #self.window = Tk()
        self.window.geometry("1440x1024")
        self.window.configure(bg = "#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            79.0,
            65.0,
            399.0,
            264.0,
            fill="#EB5757",
            outline="")

        self.canvas.create_rectangle(
            573.0,
            65.0,
            893.0,
            264.0,
            fill="#2F80ED",
            outline="")

        self.canvas.create_rectangle(
            1040.0,
            65.0,
            1360.0,
            264.0,
            fill="#F2C94C",
            outline="")

        self.canvas.create_text(
            105.0,
            94.0,
            anchor="nw",
            text="Total Employee",
            fill="#FFFFFF",
            font=("InriaSerif Regular", 24 * -1)
        )

        self.canvas.create_text(
            605.0,
            89.0,
            anchor="nw",
            text="Total In Station 1",
            fill="#FFFFFF",
            font=("InriaSerif Regular", 24 * -1)
        )

        self.canvas.create_text(
            1066.0,
            84.0,
            anchor="nw",
            text="Total In Station 2",
            fill="#000000",
            font=("InriaSerif Regular", 24 * -1)
        )

        self.canvas.create_text(
            273.0,
            152.0,
            anchor="nw",
            text=self.TotalEmployees(),
            fill="#FFFFFF",
            font=("McLaren Regular", 64 * -1)
        )

        self.canvas.create_text(
            773.0,
            147.0,
            anchor="nw",
            text="20",
            fill="#FFFDFD",
            font=("McLaren Regular", 64 * -1)
        )

        self.canvas.create_text(
            1234.0,
            142.0,
            anchor="nw",
            text="60",
            fill="#000000",
            font=("McLaren Regular", 64 * -1)
        )

        button_image_1 = PhotoImage(
            file=self.resource_path("./assets/button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.ShowForm,
            relief="flat"
        )
        button_1.place(
            x=46.0,
            y=347.0,
            width=321.0,
            height=72.0
        )
        self.addEmpBtn=button_1
        button_image_2 = PhotoImage(
            file=self.resource_path("./assets/button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=389.0,
            y=347.0,
            width=321.0,
            height=72.0
        )

        button_image_3 = PhotoImage(
            file=self.resource_path("./assets/button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=731.0,
            y=347.0,
            width=321.0,
            height=72.0
        )

        button_image_4 = PhotoImage(
            file=self.resource_path("./assets/button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command= self.ShowEmployee,
            relief="flat"
        )
        button_4.place(
            x=1083.0,
            y=347.0,
            width=321.0,
            height=72.0
        )
       
        self.MainFrame=Frame(self.window,background="Black")
        self.MainFrame.place(x=0,y=450,width=1440,height=420)
       
        self.EmployeeTable(self.MainFrame)

        self.window.resizable(False, False)
        self.window.mainloop()
    @classmethod
    def TotalEmployees(self):
        count=self.emp.TotalEmpCount()
        if count<10:
            count="0"+str(count)
        return count
            # @classmethod
    # def PopulateList(self,root):
    #     emp=employee()
    #     EmpList=emp.GetJSON()
        
    #     List=helper.ListofDict2ListofList(EmpList)
    #     heads=list(EmpList[0])
    #     List.insert(0,heads)
    #     for rows in range(len(List)):
    #         for j in range(len(List[1])):
    #             w=Text(root,width=14,height=2)
    #             w.grid(row=rows+1,column=j)
    #             w.insert(END, List[rows][j])
   
    @classmethod
    def EmployeeTable(self,root):

        emp=employee()
        EmpList=emp.GetJSON()
        List=helper.ListofDict2ListofList(EmpList)
        heads=list(EmpList[0])
        headerCount=range(1,len(heads))
         #Tree View Frame = Table to Show Employees
        frame=Frame(root)
        frame.pack(padx=20)
        
        #Vertical Scrollbar
        tv_Yscroll=Scrollbar(frame)
        tv_Yscroll.pack(side=RIGHT,fill=Y)
        #Horizontal Scrollbar
        tv_Xscroll=Scrollbar(frame,orient=HORIZONTAL)
        tv_Xscroll.pack(side=BOTTOM,fill=X)

        tv = ttk.Treeview(
        frame, 
        columns=list(headerCount), 
        show='headings', 
        height=20,
        yscrollcommand=tv_Yscroll.set,
        xscrollcommand=tv_Xscroll.set
        #height=3
        )
        tv.pack()
        
        tv_Yscroll.config(command=tv.yview)
        tv_Xscroll.config(command=tv.xview)
        
        for h in headerCount:
            tv.heading(column=h,text=heads[h])
        for i in range(len(List)):
            emp=List[i].pop(0)
            tv.insert(parent='',index=i,iid=i,values=List[i])
        tv.column("#0",stretch=False)
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        return tv

    @classmethod
    def ShowEmployee(self):
        for widget in self.MainFrame.winfo_children():
            widget.destroy()
        self.MainFrame=Frame(self.window,background="Black")
        self.MainFrame.place(x=0,y=450,width=1440,height=420)
        self.EmpTable=self.EmployeeTable(self.MainFrame)
    @classmethod
    def ShowForm(self):
        for widget in self.MainFrame.winfo_children():
            widget.destroy()
        self.MainFrame=Frame(self.window)
        self.MainFrame.place(x=0,y=450,width=1440,height=420)
        frame1=Frame(self.MainFrame,width=1400,height=400)
       # frame2=Frame(self.MainFrame,width=480,height=400,background="white")
       # frame3=Frame(self.MainFrame,width=480,height=400,background="white")
        # frame.pack(fill=None)
        frame1.pack(padx=40,pady=50)
       # frame2.grid(row=0,column=2)
       # frame2.grid(row=0,column=3)

        #name
        name_label = ttk.Label(frame1, text="Name:")
        name_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)
        global name_entry
        name_entry = ttk.Entry(frame1)
        name_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

        # fathername
        fname_label = ttk.Label(frame1, text="Father Name:")
        fname_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)
        global fname_entry
        fname_entry = ttk.Entry(frame1)
        fname_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

        #designation
        desig_label=ttk.Label(frame1,text="Designation:")
        desig_label.grid(column=0, row=3, sticky=W, padx=5, pady=5)
        global desig_entry
        desig_entry = ttk.Entry(frame1)
        desig_entry.grid(column=1, row=3, sticky=E, padx=5, pady=5)

        #station
        station_label=ttk.Label(frame1,text="Station:")
        station_label.grid(column=0, row=4, sticky=W, padx=5, pady=5)
        global station_entry
        station_entry = ttk.Entry(frame1)
        station_entry.grid(column=1, row=4, sticky=E, padx=5, pady=5)

        #BPS
        bps_label=ttk.Label(frame1,text="BPS:")
        bps_label.grid(column=2, row=0, sticky=W, padx=5, pady=5)
        global bps_entry
        bps_entry = ttk.Entry(frame1)
        bps_entry.grid(column=3, row=0, sticky=E, padx=5, pady=5)

        #CurrentBPS
        currentbps_label=ttk.Label(frame1,text="Current BPS:")
        currentbps_label.grid(column=2, row=1, sticky=W, padx=5, pady=5)
        global currentbps_entry
        currentbps_entry = ttk.Entry(frame1)
        currentbps_entry.grid(column=3, row=1, sticky=E, padx=5, pady=5)

        #DOB
        dob_label=ttk.Label(frame1,text="DOB:")
        dob_label.grid(column=2, row=3, sticky=W, padx=5, pady=5)
        global dob_entry
        dob_entry =DateEntry(frame1,selectmode='day')
        dob_entry.grid(column=3, row=3, sticky=E, padx=5, pady=5)

        #DOA
        doa_label=ttk.Label(frame1,text="DOA:")
        doa_label.grid(column=2, row=4, sticky=W, padx=5, pady=5)
        global doa_entry
        doa_entry =DateEntry(frame1,selectmode='day')
        doa_entry.grid(column=3, row=4, sticky=E, padx=5, pady=5)
        
        #DOE
        doe_label=ttk.Label(frame1,text="DOE:")
        doe_label.grid(column=2, row=5, sticky=W, padx=5, pady=5)
        global doe_entry
        doe_entry =DateEntry(frame1,selectmode='day')
        doe_entry.grid(column=3, row=5, sticky=E, padx=5, pady=5)

        #Remarks 
        remarks_label=ttk.Label(frame1,text="Remarks:")
        remarks_label.grid(column=0, row=6, sticky=W, padx=5, pady=5)
        global remarks_entry
        remarks_entry =Text(frame1,height = 5,width = 20)
        remarks_entry.grid(column=1, row=6, sticky=E, padx=5, pady=5)
        # login button
        global save_button
        save_button = ttk.Button(frame1, text="Save",command=self.SaveEmployee)
        save_button.grid(column=3, row=6, sticky=E, padx=5, pady=5)
    @classmethod
    def SaveEmployee(self):
        name=name_entry.get()
        fname=fname_entry.get()
        designation=desig_entry.get()
        station=station_entry.get()
        bps=bps_entry.get()
        currentBps=currentbps_entry.get()
        remarks=remarks_entry.get("1.0",'end-1c')
        dob=helper.StrDate(dob_entry.get_date())
        doa=helper.StrDate(doa_entry.get_date())
        doe=helper.StrDate(doe_entry.get_date())
        isNotEmpty=self.EmptyFieldMessage(name,fname,designation,station,bps,currentBps,remarks)
        isDatesValid=self.ValidateDate(dob_entry.get_date(),doa_entry.get_date(),doe_entry.get_date())
        if isNotEmpty == True and isDatesValid == True:
            id=self.emp.CreateJSON(name,fname,designation,station,bps,currentBps,dob,doa,doe,remarks)
            if id != "":
                self.ClearFields()
                messagebox.showinfo("Employee Created!","Information of "+name+" has been saved!")

            else:
                messagebox.showerror("Not Saved!","Some Error ocurred while saving data!")

    @classmethod
    def EmptyFieldMessage(self,name,fname,designation,station,bps,currentBps,remarks)->BOOLEAN:
        if name=="":
            messagebox.showerror("Empty Field!","Name can not be left empty!")
            return False
        elif fname=="":
            messagebox.showerror("Empty Field!","Father Name can not be left empty!")
            return False
        elif designation=="":
            messagebox.showerror("Empty Field!","Designation can not be left empty!")
            return False
        elif station=="":
            messagebox.showerror("Empty Field!","Station can not be left empty!")
            return False
        elif bps=="":
            messagebox.showerror("Empty Field!","BPS can not be left empty!")
            return False
        elif currentBps=="":
            messagebox.showerror("Empty Field!","Current BPS can not be left empty!")
            return False
        elif remarks=="":
            messagebox.showerror("Empty Field!","Remarks can not be left empty!")
            return False
        else:
            return True

    
    @classmethod
    def ValidateDate(self,DOB:date,DOA:date,DOE:date):
        if DOB ==date.today():
            messagebox.showerror("Invalid Date of Birth","Date of Birth should not be a present date!")
            return False
        elif helper.calculate_age(DOB)<18:
            messagebox.showerror("Invalid Date of Birth","Date of Birth should be more than 18 years from today!")
            return False
        elif DOA > date.today():
            messagebox.showerror("Future Date Error!","Date of Assigned can not be a future date")
            return False
        elif DOE > date.today():
            messagebox.showerror("Future Date Error!","Date of Entry can not be a future date")
            return False
        else:
            return True
    
    @classmethod
    def ClearFields(self):
        name_entry.delete(0,'end')
        fname_entry.delete(0,'end')
        desig_entry.delete(0,'end')
        station_entry.delete(0,'end')
        bps_entry.delete(0,'end')
        currentbps_entry.delete(0,'end')
        remarks_entry.delete('1.0', END)
        dob_entry.set_date(date.today())
        doa_entry.set_date(date.today())
        doe_entry.get_date(date.today())