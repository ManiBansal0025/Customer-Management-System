import pymysql
mycon = pymysql.connect(host="localhost", user="root", password="root1234", database="cms_mani")

class Customer:
    def __init__(self):
        self.id = 0
        self.name=""
        self.age = 0
        self.mobile = ""
    def add_cus(self):
        mycur = mycon.cursor()
        qry = f"insert into cus values({self.id},'{self.name}',{self.age},'{self.mobile}')"
        mycur.execute(qry)
        mycon.commit()
    def search_cus(self,id):
        mycur = mycon.cursor()
        qry = "Select * from cus where id=%s"
        mycur.execute(qry,self.id)
        row = mycur.fetchone()
        self.name = row[1]
        self.age = row[2]
        self.mobile = row[3]
    def modify_cus(self,id):
        mycur = mycon.cursor()
        qry = "update cus set name=%s,age=%s,mobile=%s where id=%s"
        mycur.execute(qry,(self.name,self.age,self.mobile,self.id))
        mycon.commit()
    def delete_cus(self,id):
        mycur = mycon.cursor()
        qry = "delete from cus where id=%s"
        mycur.execute(qry,self.id)
        mycon.commit()
    def showall_cus(self):
        mycur=mycon.cursor()
        qry = "select * from cus"
        mycur.execute(qry)
        row = mycur.fetchall()

        mycon.commit()


import tkinter
import PIL
from PIL import Image,ImageTk
import tkinter.messagebox

root = tkinter.Tk()
root.config(bg="light green")
varid = tkinter.IntVar()
varname = tkinter.StringVar()
varage = tkinter.IntVar()
varmob = tkinter.StringVar()

def btn_add_click():
    obj = Customer()
    obj.id = varid.get()
    obj.name = varname.get()
    obj.age = varage.get()
    obj.mobile = varmob.get()
    if(obj.id==0 or obj.name=="" or obj.age==0 or obj.mobile=="" ):
        tkinter.messagebox.showerror("Not filled","All entries are not filled")
    else:
        obj.add_cus()
        tkinter.messagebox.showinfo("Sucess","Customer Added Sucessfully")
def btn_search_click():
    obj = Customer()
    obj.id = varid.get()
    if(obj.id == 0):
        tkinter.messagebox.showwarning("ID require","For searching customer you have to fill id")
    else:
        obj.search_cus(obj.id)
        tkinter.Label(root,text=f"id = {obj.id}   name = {obj.name}   age = {obj.age}   mobile no. = {obj.mobile}",fg="green",
                      font=("Georgia",24),bg="white").pack(side="bottom",pady=10)
def btn_modify_click():
    obj = Customer()
    obj.id = varid.get()
    obj.name = varname.get()
    obj.age = varage.get()
    obj.mobile = varmob.get()
    if (obj.id == 0 or obj.name=="" or obj.age==0 or obj.mobile==""):
        tkinter.messagebox.showwarning("Not filled","All entries are not filled")
    else:
        obj.modify_cus(obj.id)
        tkinter.messagebox.showinfo("Sucess", "Customer Modified Sucessfully")
def btn_delete_click():
    obj = Customer()
    obj.id = varid.get()
    if(obj.id==0):
        tkinter.messagebox.showwarning("ID require","For deleting customer you have to fill id")
    else:
        obj.delete_cus(obj.id)
        tkinter.messagebox.showinfo("Sucess", "Customer Deleted Sucessfully")
def btn_showall_click():
    obj = Customer()
    obj.showall_cus()
def btn_exit_click():
    Msgbox = tkinter.messagebox.askquestion("Exit","Do you want to Exit?")
    if(Msgbox == 'yes'):
        root.destroy()

root.title("Customer Management System")
#root.geometry('1200x1100')
#Main title frame
frame1 = tkinter.Frame(root,bg="dark green")
frame1.pack(fill='y',side="top")
#second label and entry widget
frame2 = tkinter.Frame(root,bg="white")
frame2.pack(pady=20,padx=20)
#third button frame
frame3 = tkinter.Frame(root,bg="white")
frame3.pack(padx=20,side="bottom",fill='y')


#===========================================Main title and image========================================
lbl1 = tkinter.Label(frame1,text="Customer  Management  System",bg="dark green",font=("Arial bold",36))
lbl1.grid(row=0,column=1)
img_load = Image.open("logo.png")
image_cus = ImageTk.PhotoImage(img_load)
lbl2 = tkinter.Label(frame1,image=image_cus)
lbl2.grid(row=0,column=0)


#=======================================Labels=================================================
lblent = tkinter.Label(frame2,text="Enter the details as mentioned below:",bg="dark green", font=("Georgia",25))
lblent.grid(row=1,column=1)
lbl_id = tkinter.Label(frame2,text = "CUSTOMER ID",fg="dark green", font=("Georgia",24),bg="white")
lbl_id.grid(row=2,column=1,pady="10")
lbl_name = tkinter.Label(frame2,text = "NAME",fg="dark green", font=("Georgia",24),bg="white")
lbl_name.grid(row=3,column=1,pady="10")
lbl_age = tkinter.Label(frame2,text = "AGE",fg="dark green", font=("Georgia",24),bg="white")
lbl_age.grid(row=4,column=1,pady="10")
lbl_mob = tkinter.Label(frame2,text = "MOBILE NO.",fg="dark green",font=("Georgia",24),bg="white")
lbl_mob.grid(row=5,column=1,pady="10")

#===================================Entry=========================================================
ent_id = tkinter.Entry(frame2,textvariable=varid,bg="dark green",font=("Georgia",20),bd=10)
ent_id.grid(row=2,column=2)
ent_name = tkinter.Entry(frame2,textvariable=varname,bg="dark green", font=("Georgia",20),bd=10)
ent_name.grid(row=3,column=2)
ent_age = tkinter.Entry(frame2,textvariable=varage,bg="dark green", font=("Georgia",20),bd=10)
ent_age.grid(row=4,column=2)
ent_mob = tkinter.Entry(frame2,textvariable=varmob,bg="dark green", font=("Georgia",20),bd=10)
ent_mob.grid(row=5,column=2)

#==========================================Button=================================================
btn_add = tkinter.Button(frame3,text="ADD",bg="dark green",relief="groove",font=("Georgia",15),bd=10,command=btn_add_click)
btn_add.grid(row=7,column=0)
btn_search = tkinter.Button(frame3,text="SEARCH",bg="dark green",relief="groove",font=("Georgia",15),bd=10,command=btn_search_click)
btn_search.grid(row=7,column=1)
btn_modify = tkinter.Button(frame3,text="MODIFY",bg="dark green",relief="groove",font=("Georgia",15),bd=10,command=btn_modify_click)
btn_modify.grid(row=7,column=2)
btn_delete = tkinter.Button(frame3,text="DELETE",bg="dark green",relief="groove",font=("Georgia",15),bd=10,command=btn_delete_click)
btn_delete.grid(row=7,column=3)
btn_showall = tkinter.Button(frame3,text="SHOW ALL",bg="dark green",relief="groove",font=("Georgia",15),bd=10,command=btn_showall_click)
btn_showall.grid(row=7,column=4)
btn_exit = tkinter.Button(frame3,text="EXIT",bg="dark green",relief="groove",font=("Georgia",15),bd=10,command=btn_exit_click)
btn_exit.grid(row=8,column=2)

###############################################image################################################################


root.mainloop()
#search remove from screen
#showall problem
