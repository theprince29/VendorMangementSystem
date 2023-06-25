from ast import Delete
import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

class supplclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Shop-Management System")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        self.root.focus_force()

        ##------------all variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_status=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contacts=StringVar()
        ## Search=frame---
        Searchframe=LabelFrame(self.root,text="Search Supplier",font=("goudy old style",12,"bold"),bg="white")
        Searchframe.place(x=250,y=50,width=600,height=70)

        lbl_search=Label(Searchframe,text="Search by Supplier_Id.",bg="white",font=("goudy old style",15))
        lbl_search.place(x=10,y=10)

        txt_search=Entry(Searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10,width=180)
        btn_search=Button(Searchframe,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white").place(x=390,y=8,height=28)

        ## Title------
        title=Label(self.root,text="Suppliers Details",bg="#0f4d7d",font=("goudy old style",20,"bold"),fg="white").place(x=50,y=10,width=1000)

        ##content-----
        #Row1-----
        lbl_supplier_invoice=Label(self.root,text="Supplier Id.",bg="white",font=("goudy old style",15)).place(x=50,y=150)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,state='readonly',bg="white",font=("goudy old style",15)).place(x=160,y=150,width=180)
        #Row2--------
        lbl_name=Label(self.root,text="Supplier-Name",bg="white",font=("goudy old style",15)).place(x=380,y=150)
        txt_name=Entry(self.root,textvariable=self.var_name,bg="white",state='readonly',font=("goudy old style",15)).place(x=530,y=150,width=180)
        #Row3===
        lbl_contact=Label(self.root,text="Contact",bg="white",font=("goudy old style",15)).place(x=780,y=150)
        txt_contact=Entry(self.root,textvariable=self.var_contacts,bg="white",state='readonly',font=("goudy old style",15)).place(x=850,y=150,width=180)
        #Row4------
        lbl_desc=Label(self.root,text="Supplier_Add.",font=("times new roman",15),bg="white").place(x=50,y=240)
        self.txt_desc=Text(self.root,bg="lightyellow",font=("goudy old style",15))
        self.txt_desc.place(x=180,y=240,width=300,height=60)

        #buttons-----------
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=640,y=280,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=280,width=110,height=28)

        #tree view---
        cst_frame=Frame(self.root,bd=3,relief=RIDGE)
        cst_frame.place(x=0,y=320,relwidth=1,height=170)

        scrolly=Scrollbar(cst_frame,orient=VERTICAL)
        scrollx=Scrollbar(cst_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(cst_frame,columns=("invoice","name","contact","desc","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        self.SupplierTable.heading("invoice",text="Supplier_Id.")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("desc",text="Sup._Address")
        self.SupplierTable.heading("status",text="Status")
       

        self.SupplierTable['show']="headings"

        self.SupplierTable.column("invoice",width=20)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=40)
        self.SupplierTable.column("desc",width=100)
        self.SupplierTable.column("status",width=70)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#=============================================================================
    
    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  

    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contacts.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])
        

    
    def delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Supplier_Id. is Must!",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid Supplier_Id. !",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully!!",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contacts.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Supplier_Id. should be required",parent=self.root) 
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=supplclass(root)
    root.mainloop()