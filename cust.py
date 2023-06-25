from ast import Delete
from optparse import Values
import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from turtle import width
from PIL import Image,ImageTk

class custclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Shop-Management System")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        self.root.focus_force()

        ##------------all variables
        self.var_cust_id=StringVar()
        self.var_name=StringVar()
        self.var_contacts=StringVar()
        self.var_pass=StringVar()
        self.var_searchtxt=StringVar()
        ## Title------
        title=Label(self.root,text="Customer Details",bg="#0f4d7d",font=("goudy old style",15),fg="white").place(x=50,y=16,width=1000)

        ##content-----
        lbl_title=Label(self.root,text="Customer Id",bg="white",font=("goudy old style",15)).place(x=50,y=150)
        lbl_name=Label(self.root,text="Customer-Name",bg="white",font=("goudy old style",15)).place(x=380,y=150)
        lbl_contact=Label(self.root,text="Contact",bg="white",font=("goudy old style",15)).place(x=780,y=150)
       
        txt_title=Entry(self.root,textvariable=self.var_cust_id,bg="white",state='readonly',font=("goudy old style",15)).place(x=160,y=150,width=180)
        txt_name=Entry(self.root,textvariable=self.var_name,state='readonly',justify=CENTER,font=("goudy old style",15))
        txt_name.place(x=530,y=150,width=180)
        
        txt_contact=Entry(self.root,textvariable=self.var_contacts,state='readonly',justify=CENTER,font=("goudy old style",15))
        txt_contact.place(x=850,y=150,width=180)
        

        #Row2--------
        lbl_gov_id=Label(self.root,text="Email-Id.",bg="white",font=("goudy old style",15)).place(x=50,y=200)
        
        txt_email=Entry(self.root,textvariable=self.var_pass,state='readonly',bg="white",font=("goudy old style",15)).place(x=160,y=200,width=180)
        

        ## Search=frame---
        Searchframe=LabelFrame(self.root,text="Search Customer",font=("goudy old style",12,"bold"),bg="white")
        Searchframe.place(x=250,y=50,width=600,height=70)

        lbl_search=Label(Searchframe,text="Search by Customer_Id.",bg="white",font=("goudy old style",15))
        lbl_search.place(x=10,y=10)

        txt_search=Entry(Searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10,width=180)
        btn_search=Button(Searchframe,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white").place(x=390,y=8,height=28)

        #Row3------
        lbl_address=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=380,y=200)
        self.txt_address=Text(self.root,bg="lightyellow",font=("goudy old style",15))
        self.txt_address.place(x=530,y=200,width=300,height=60)

        #buttons-----------
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=50,y=280,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=920,y=280,width=110,height=28)

        #tree view---
        cst_frame=Frame(self.root,bd=3,relief=RIDGE)
        cst_frame.place(x=0,y=320,relwidth=1,height=170)

        scrolly=Scrollbar(cst_frame,orient=VERTICAL)
        scrollx=Scrollbar(cst_frame,orient=HORIZONTAL)

        self.CustomerTable=ttk.Treeview(cst_frame,columns=("cid","Name","contact","email","govid","Idno","Address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
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

        self.CustomerTable.column("cid",width=90)
        #self.CustomerTable.column("utype",width=90)
        self.CustomerTable.column("Name",width=100)
        self.CustomerTable.column("contact",width=100)
        self.CustomerTable.column("email",width=100)
        self.CustomerTable.column("govid",width=100)
        self.CustomerTable.column("Idno",width=100)        
        self.CustomerTable.column("Address",width=100)
        self.CustomerTable.pack(fill=BOTH,expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#=============================================================================
    
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
        
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[6])

    
    def delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_cust_id.get()=="":
                messagebox.showerror("Error","Customer Id is Must!",parent=self.root)
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

    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Customer_Id. should be required",parent=self.root) 
            else:
                cur.execute("select cust_Id ,f_name,contact ,email,govid,Idno,Address from register where cust_Id=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.CustomerTable.delete(*self.CustomerTable.get_children())
                    self.CustomerTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def clear(self):
        self.var_cust_id.set("")
        self.var_name.set("")
        self.var_contacts.set("")
        self.var_pass.set("")
        self.txt_address.delete('1.0',END)
        self.show()

       


if __name__=="__main__":
    root=Tk()
    obj=custclass(root)
    root.mainloop()