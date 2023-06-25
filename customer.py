from ast import Delete
from optparse import Values
import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from turtle import width
from PIL import Image,ImageTk
import os

class customerclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+150+80")
        self.root.title("Shop-Management System")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        self.root.focus_force()

        ##------------all variables
        self.var_cust_id=StringVar()
        self.var_name=StringVar()
        self.var_Anygov_id=StringVar()
        self.var_contacts=StringVar()
        self.var_pass=StringVar()
        self.var_Id_No=StringVar()
        self.var_utype=StringVar()

        # self.cat_list=[]
        # self.sup_list=[]
        # self.fetch_cat_sup()

        ## Title------
        title=Label(self.root,text="Customer Can Update and Save his\her Information Here",bg="white",font=("goudy old style",15),fg="blue").place(x=40,y=16,width=1000)
        title=Label(self.root,text="Customer Details",bg="#0f4d7d",font=("goudy old style",15),fg="white").place(x=10,y=50,width=1080)

        ##content-----
        title=Label(self.root,text="Note : Password must be Required !\n\t    It is same as at the time of registration!!",bg="white",font=("goudy old style",15),fg="red").place(x=450,y=80)
        #Row1-----
        lbl_utype=Label(self.root,text="Password",bg="white",font=("goudy old style",15)).place(x=50,y=100)
        lbl_title=Label(self.root,text="Customer Id",bg="white",font=("goudy old style",15)).place(x=50,y=150)
        lbl_name=Label(self.root,text="Customer-Name",bg="white",font=("goudy old style",15)).place(x=380,y=150)
        lbl_contact=Label(self.root,text="Contact",bg="white",font=("goudy old style",15)).place(x=780,y=150)
       
        txt_title=Entry(self.root,textvariable=self.var_cust_id,bg="white",state='readonly',font=("goudy old style",15)).place(x=160,y=150,width=180)
        txt_name=Entry(self.root,textvariable=self.var_name,state='readonly',justify=CENTER,font=("goudy old style",15))
        txt_name.place(x=530,y=150,width=180)
        
        txt_contact=Entry(self.root,textvariable=self.var_contacts,state='readonly',justify=CENTER,font=("goudy old style",15))
        txt_contact.place(x=850,y=150,width=180)
        
        #User type====
        txt_utype=Entry(self.root,textvariable=self.var_utype,justify=CENTER,font=("goudy old style",15),bg="light gray")
        txt_utype.place(x=160,y=100,width=180)
        

        #Row2--------
        lbl_gov_id=Label(self.root,text="Email-Id.",bg="white",font=("goudy old style",15)).place(x=50,y=200)
        lbl_Password=Label(self.root,text="Gov-Id No.",bg="white",font=("goudy old style",15)).place(x=760,y=200)
        lbl_govid=Label(self.root,text="Any Gov-Id",bg="white",font=("goudy old style",15)).place(x=380,y=200)
       
        cmb_gov_id=ttk.Combobox(self.root,textvariable=self.var_Anygov_id,values=("Select","Aadhar Card","PAN Card","Voter-Id","Any-Other"),state='readonly',justify=CENTER)
        cmb_gov_id.place(x=530,y=200,width=180,height=28)
        cmb_gov_id.current(0)
        txt_email=Entry(self.root,textvariable=self.var_pass,bg="white",font=("goudy old style",15)).place(x=160,y=200,width=180)
        txt_govid=Entry(self.root,textvariable=self.var_Id_No,bg="white",font=("goudy old style",15)).place(x=850,y=200,width=180)

        #Row3------
        lbl_address=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=50,y=240)
        self.txt_address=Text(self.root,bg="lightyellow",font=("goudy old style",15))
        self.txt_address.place(x=160,y=240,width=300,height=60)

        #buttons-----------
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=620,y=280,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=500,y=280,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=280,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=280,width=110,height=28)
        btn_clear=Button(self.root,text="Proceed to the Shopping Page =>",command=self.proceed,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=120,y=330,width=280,height=32)

        #tree view---
        cst_frame=Frame(self.root,bd=3,relief=RIDGE)
        cst_frame.place(x=0,y=380,relwidth=1,height=85)

        scrolly=Scrollbar(cst_frame,orient=VERTICAL)
        scrollx=Scrollbar(cst_frame,orient=HORIZONTAL)

        self.CustomerTable=ttk.Treeview(cst_frame,columns=("cid","Name","contact","email","govid","Idno","Address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        #scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)
        self.CustomerTable.heading("cid",text="Cust.-Id")
        #self.CustomerTable.heading("utype",text="User_Type")
        self.CustomerTable.heading("Name",text="Name")
        self.CustomerTable.heading("contact",text="Contact")
        self.CustomerTable.heading("email",text="Email")
        self.CustomerTable.heading("govid",text="Gov-Id")
        self.CustomerTable.heading("Idno",text="Gov-Id No.")
        self.CustomerTable.heading("Address",text="Address")

        self.CustomerTable['show']="headings"

        self.CustomerTable.column("cid",width=50)
        #self.CustomerTable.column("utype",width=90)
        self.CustomerTable.column("Name",width=100)
        self.CustomerTable.column("contact",width=50)
        self.CustomerTable.column("email",width=100)
        self.CustomerTable.column("govid",width=50)
        self.CustomerTable.column("Idno",width=100)        
        self.CustomerTable.column("Address",width=100)
        self.CustomerTable.pack(fill=BOTH,expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        footer=Label(self.root,text="Vendors Management System | Developed by Nexus Pvt. Ltd\nFor any Issue Regarding this Contact Tech. Assistant",font=("times new roman",10),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

#=============================================================================
    def add(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_cust_id.get()=="":
                messagebox.showerror("Error","Customer Id is Must!",parent=self.root)
            else:
                cur.execute("Select * from employee where  Idno=? ",(self.var_Id_No.get(),))
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","This customer is Already Exist !",parent=self.root)
                else:
                    cur.execute("Select * from register where password=?",(self.var_utype.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid Password !!",parent=self.root)
                    else:

                        cur.execute("Insert into employee (cid,Name,contact,email,govid,Idno,Address) values(?,?,?,?,?,?,?)",
                            (self.var_cust_id.get(),
                            #self.var_utype.get(),
                            self.var_name.get(),
                            self.var_contacts.get(),
                            self.var_pass.get(),
                            self.var_Anygov_id.get(),
                            self.var_Id_No.get(),
                            self.txt_address.get('1.0',END)
                            ))

                        con.commit()
                        messagebox.showinfo("Success!","Customer is Succesfully Added!!",parent=self.root) 
                self.show()       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("Select cust_Id ,f_name,contact ,email,govid,Idno,Address from register")
            rows=cur.fetchall()
            self.CustomerTable.delete(*self.CustomerTable.get_children())
            for row in rows:
                self.CustomerTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  

    def get_data(self,ev):
        f=self.CustomerTable.focus()
        content=(self.CustomerTable.item(f))
        row=content['values']
        self.var_cust_id.set(row[0])
        
        self.var_name.set(row[1])
        self.var_contacts.set(row[2])
        self.var_pass.set(row[3])
        self.var_Anygov_id.set(row[4])
        self.var_Id_No.set(row[5])
        
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[6])

    def update(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_cust_id.get()=="":
                messagebox.showerror("Error","Customer Id is Must!",parent=self.root)
            else:
                cur.execute("Select * from register where password=?",(self.var_utype.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid Password !!",parent=self.root)
                else:
                    cur.execute("Update register set govid=?,Idno=?,Address=? where cust_Id=?",
                        (
                        # self.var_name.get(),
                        # self.var_contacts.get(),
                        self.var_Anygov_id.get(),
                        self.var_Id_No.get(),
                        # self.var_pass.get(),
                        self.txt_address.get('1.0',END),
                        self.var_cust_id.get()
                        ))

                    con.commit()
                    messagebox.showinfo("Success!","Customer is Succesfully Updated!!",parent=self.root) 
                self.show()       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_cust_id.get()=="":
                messagebox.showerror("Error","Customer Id is Must!",parent=self.root)
            else:
                cur.execute("Select * from register where password=?",(self.var_utype.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid Password !",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from register where cust_Id=?",(self.var_cust_id.get(),))
                        cur.execute("delete from employee where cid=?",(self.var_cust_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Customer Deleted Successfully!!",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_cust_id.set("")
        self.var_utype.set("Enter Password")
        self.var_name.set("")
        self.var_contacts.set("")
        self.var_Anygov_id.set("Select")
        self.var_Id_No.set("")
        self.var_pass.set("")
        self.txt_address.delete('1.0',END)
        self.show()

    def proceed(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor() 
        cur.execute("Select * from register where password=?",(self.var_utype.get(),))
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("Error","Please Verify Yourself by Entering your Password!!!",parent=self.root)
        else:
            self.root.destroy()
            os.system("python bill.py")
        

if __name__=="__main__":
    root=Tk()
    obj=customerclass(root)
    root.mainloop()