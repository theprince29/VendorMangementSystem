from ast import Delete
from optparse import Values
import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from turtle import width
from PIL import Image,ImageTk

class dealer_class:
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
        title=Label(self.root,text="Dealers Details",bg="#0f4d7d",font=("goudy old style",15),fg="white").place(x=50,y=16,width=1000)

        ##content-----
        lbl_title=Label(self.root,text="Unique Id",bg="white",font=("goudy old style",15)).place(x=50,y=150)
        lbl_name=Label(self.root,text="Dealer-Name",bg="white",font=("goudy old style",15)).place(x=380,y=150)
        lbl_contact=Label(self.root,text="Contact",bg="white",font=("goudy old style",15)).place(x=780,y=150)
       
        txt_title=Entry(self.root,textvariable=self.var_cust_id,bg="white",state='readonly',font=("goudy old style",15)).place(x=160,y=150,width=180)
        txt_name=Entry(self.root,textvariable=self.var_name,state='readonly',justify=CENTER,font=("goudy old style",15))
        txt_name.place(x=530,y=150,width=180)
        
        txt_contact=Entry(self.root,textvariable=self.var_contacts,state='readonly',justify=CENTER,font=("goudy old style",15))
        txt_contact.place(x=850,y=150,width=180)
        

        #Row2--------
        lbl_gov_id=Label(self.root,text="Email-Id.",bg="white",font=("goudy old style",15)).place(x=50,y=200)
        
        txt_email=Entry(self.root,textvariable=self.var_pass,bg="white",state='readonly',font=("goudy old style",15)).place(x=160,y=200,width=180)
        

        ## Search=frame---
        Searchframe=LabelFrame(self.root,text="Search Dealer",font=("goudy old style",12,"bold"),bg="white")
        Searchframe.place(x=250,y=50,width=600,height=70)

        lbl_search=Label(Searchframe,text="Search by Unique_Id.",bg="white",font=("goudy old style",15))
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

        self.dealer_table=ttk.Treeview(cst_frame,columns=("uid","name","contact","gov_id","id_no","email","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.dealer_table.xview)
        scrolly.config(command=self.dealer_table.yview)
        self.dealer_table.heading("uid",text="Unique-Id")
        self.dealer_table.heading("name",text="Name")
        self.dealer_table.heading("contact",text="Contact")
        self.dealer_table.heading("gov_id",text="Gov_Id")
        self.dealer_table.heading("id_no",text="Gov_Id No.")
        self.dealer_table.heading("email",text="Email")
        self.dealer_table.heading("address",text="Address")
        self.dealer_table['show']="headings"

        self.dealer_table.column("uid",width=90)
        self.dealer_table.column("name",width=100)
        self.dealer_table.column("contact",width=100)
        self.dealer_table.column("gov_id",width=100)
        self.dealer_table.column("id_no",width=100)
        self.dealer_table.column("email",width=100)        
        self.dealer_table.column("address",width=100)
        self.dealer_table.pack(fill=BOTH,expand=1,)
        self.dealer_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#=============================================================================
    
    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("Select did, name ,contact ,gov_id ,id_no ,email ,address  from dealer")
            rows=cur.fetchall()
            self.dealer_table.delete(*self.dealer_table.get_children())
            for row in rows:
                self.dealer_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  

    def get_data(self,ev):
        f=self.dealer_table.focus()
        content=(self.dealer_table.item(f))
        row=content['values']
        self.var_cust_id.set(row[0])
        
        self.var_name.set(row[1])
        self.var_contacts.set(row[2])
        self.var_pass.set(row[5])
        
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[6])

    
    def delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_cust_id.get()=="":
                messagebox.showerror("Error","Unique Id is Must!",parent=self.root)
            else:
                cur.execute("Select * from dealer where email=?",(self.var_pass.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid Password !",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from dealer where did=?",(self.var_cust_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","User Deleted Successfully!!",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Unique_Id. must be Required!!",parent=self.root) 
            else:
                cur.execute("select did, name ,contact ,gov_id ,id_no ,email ,address  from dealer where did=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.dealer_table.delete(*self.dealer_table.get_children())
                    self.dealer_table.insert('',END,values=row)
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
        self.var_searchtxt.set("")
        self.show()

       


if __name__=="__main__":
    root=Tk()
    obj=dealer_class(root)
    root.mainloop()