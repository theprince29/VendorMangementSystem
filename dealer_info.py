from ast import Delete
import os
import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

class Dealer_infoclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+150+80")
        self.root.title("Shop-Management System")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        self.root.focus_force()

        ##------------all variables
        self.var_unique_id=StringVar()
        self.var_name=StringVar()
        self.var_contacts=StringVar()
        self.var_email=StringVar()
        self.var_Anygov_id=StringVar()
        self.var_Id_No=StringVar()

        self.var_pass=StringVar()
        
        

        # self.cat_list=[]
        # self.sup_list=[]
        # self.fetch_cat_sup()

        ## Title------
        title=Label(self.root,text="Dealer Can Update his\her Information Here",bg="white",font=("goudy old style",15),fg="blue").place(x=40,y=50,width=1000)
        title=Label(self.root,text="Dealer Info Window",bg="#0f4d7d",font=("goudy old style",17),fg="white").place(x=20,y=16,width=1060)

        ##content-----
        title=Label(self.root,text="Note : Password must be Required !!",bg="white",font=("goudy old style",15),fg="red").place(x=450,y=90)
        #Row1-----
        lbl_pass=Label(self.root,text="Password",bg="white",font=("goudy old style",15)).place(x=50,y=100)

        lbl_title=Label(self.root,text="Unique Id",bg="white",font=("goudy old style",15)).place(x=50,y=150)
        lbl_name=Label(self.root,text="Name",bg="white",font=("goudy old style",15)).place(x=380,y=150)
        lbl_contact=Label(self.root,text="Contact",bg="white",font=("goudy old style",15)).place(x=780,y=150)
       
        txt_title=Entry(self.root,textvariable=self.var_unique_id,bg="white",state='readonly',font=("goudy old style",15)).place(x=160,y=150,width=180)
        txt_name=Entry(self.root,textvariable=self.var_name,state='readonly',justify=CENTER,font=("goudy old style",15))
        txt_name.place(x=530,y=150,width=180)
        txt_contact=Entry(self.root,textvariable=self.var_contacts,justify=CENTER,font=("goudy old style",15))
        txt_contact.place(x=850,y=150,width=180)
        #Row2--------
        lbl_email=Label(self.root,text="Email-Id.",bg="white",font=("goudy old style",15)).place(x=50,y=200)
        lbl_govid=Label(self.root,text="Any Gov-Id",bg="white",font=("goudy old style",15)).place(x=380,y=200)
        lbl_gov_idno=Label(self.root,text="Gov-Id No.",bg="white",font=("goudy old style",15)).place(x=760,y=200)
        
        txt_password=Entry(self.root,textvariable=self.var_pass,justify=CENTER,font=("goudy old style",15),bg="light gray")
        txt_password.place(x=160,y=100,width=180)
        
        cmb_gov_id=Entry(self.root,textvariable=self.var_Anygov_id,state='readonly',justify=CENTER)
        cmb_gov_id.place(x=530,y=200,width=180,height=28)
        
        txt_govid=Entry(self.root,textvariable=self.var_Id_No,bg="white",state='readonly',font=("goudy old style",15)).place(x=850,y=200,width=180)
        txt_email=Entry(self.root,textvariable=self.var_email,bg="white",font=("goudy old style",15)).place(x=160,y=200,width=180)
        
        #Row3------
        lbl_address=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=50,y=240)
        self.txt_address=Text(self.root,bg="lightyellow",font=("goudy old style",15))
        self.txt_address.place(x=160,y=240,width=300,height=60)

        #buttons-----------
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=580,y=280,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=720,y=280,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=280,width=110,height=28)
        btn_clear=Button(self.root,text="Proceed",command=self.search,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=100,width=90,height=28)

        #tree view---
        cst_frame=Frame(self.root,bd=3,relief=RIDGE)
        cst_frame.place(x=0,y=380,relwidth=1,height=85)

        scrolly=Scrollbar(cst_frame,orient=VERTICAL)
        scrollx=Scrollbar(cst_frame,orient=HORIZONTAL)

        self.DealerTable=ttk.Treeview(cst_frame,columns=("uid","name","contact","gov_id","id_no","email","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        #scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.DealerTable.xview)
        scrolly.config(command=self.DealerTable.yview)
        self.DealerTable.heading("uid",text="Unique-Id")
        self.DealerTable.heading("name",text="Name")
        self.DealerTable.heading("contact",text="Contact")
        self.DealerTable.heading("gov_id",text="Gov_Id")
        self.DealerTable.heading("id_no",text="Gov_Id No.")
        self.DealerTable.heading("email",text="Email")
        self.DealerTable.heading("address",text="Address")

        self.DealerTable['show']="headings"

        self.DealerTable.column("uid",width=90)
        self.DealerTable.column("name",width=100)
        self.DealerTable.column("contact",width=100)
        self.DealerTable.column("gov_id",width=100)
        self.DealerTable.column("id_no",width=100)
        self.DealerTable.column("email",width=100)        
        self.DealerTable.column("address",width=100)
        self.DealerTable.pack(fill=BOTH,expand=1,)
        self.DealerTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        footer=Label(self.root,text="Vendors Management System | Developed by Nexus Pvt. Ltd\nFor any Issue Regarding this Contact Tech. Assistant",font=("times new roman",10),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

#=============================================================================
   
    def clear(self):
        self.var_unique_id.set("")
        self.var_name.set("")
        self.var_contacts.set("")
        self.var_email.set("")
        self.var_Anygov_id.set("Select")
        self.var_Id_No.set("")
        self.var_pass.set("")
        self.txt_address.delete('1.0',END)

    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("Select did, name ,contact ,gov_id ,id_no ,email ,address  from dealer")
            rows=cur.fetchall()
            self.DealerTable.delete(*self.DealerTable.get_children())
            for row in rows:
                self.DealerTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  

    def get_data(self,ev):
        f=self.DealerTable.focus()
        content=(self.DealerTable.item(f))
        row=content['values']
        self.var_unique_id.set(row[0])
        self.var_name.set(row[1])
        self.var_contacts.set(row[2])
        self.var_email.set(row[5])
        self.var_Anygov_id.set(row[3])
        self.var_Id_No.set(row[4])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[6])

    def update(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_unique_id.get()=="":
                messagebox.showerror("Error","Unique Id is Must!",parent=self.root)
            else:
                cur.execute("Select * from dealer where password=?",(self.var_pass.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid Password !!",parent=self.root)
                else:
                    cur.execute("Update dealer set contact=?,email=?,Address=? where did=?",
                        (self.var_contacts.get(),
                        self.var_email.get(),
                        self.txt_address.get('1.0',END),
                        self.var_unique_id.get()
                        ))

                    con.commit()
                    messagebox.showinfo("Success!","User is Succesfully Updated!!",parent=self.root) 
                self.show()       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_unique_id.get()=="":
                messagebox.showerror("Error","Unique Id is Must!",parent=self.root)
            else:
                cur.execute("Select * from dealer where password=?",(self.var_pass.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid Password !",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from dealer where did=?",(self.var_unique_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","User Deleted Successfully!!",parent=self.root)
                        self.clear()
                        messagebox.showinfo("Confirm","Your Details Has been Succesfully Deleted\nThanks for Connecting with us!!")
                        self.root.destroy()
                        os.system("python first.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_pass.get()=="":
                messagebox.showerror("Error","Password must be Required!!",parent=self.root) 
            else:
                cur.execute("select * from dealer where password=?",(self.var_pass.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.DealerTable.delete(*self.DealerTable.get_children())
                    self.DealerTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Dealer_infoclass(root)
    root.mainloop()