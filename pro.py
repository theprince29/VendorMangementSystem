from ast import Delete
from cgitb import text
import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from category import categoryclass

class proclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+150+80")
        self.root.title("Shop-Management System")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        self.root.focus_force()

        #====variables======
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_price=StringVar()
        self.var_name=StringVar()
        self.var_status=StringVar()

        #product frame===
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)

        ## Title------
        title=Label(product_frame,text=" Product Details",bg="#0f4d7d",font=("goudy old style",18),fg="white").pack(side=TOP,fill=X)
        
        lbl_category=Label(product_frame,text="Category",bg="white",font=("goudy old style",18)).place(x=30,y=80)
        lbl_product=Label(product_frame,text="Name",bg="white",font=("goudy old style",18)).place(x=30,y=150)
        lbl_price=Label(product_frame,text="Price",bg="white",font=("goudy old style",18)).place(x=30,y=230)
        lbl_status=Label(product_frame,text="Status",bg="white",font=("goudy old style",18)).place(x=30,y=300)

        #====options======
        cmb_cat=Entry(product_frame,textvariable=self.var_cat,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=80,width=200)

        txt_name=Entry(product_frame,textvariable=self.var_name,state='readonly',justify=CENTER,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,state='readonly',justify=CENTER,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=200)
        
        cmb_status=ttk.Entry(product_frame,textvariable=self.var_status,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=300,width=200)
        

        #buttons-----------
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=20,y=400,width=100,height=40)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=320,y=400,width=100,height=40)

        ## Search=frame---
        Searchframe=LabelFrame(self.root,text="Search Product",font=("goudy old style",12,"bold"),bg="white")
        Searchframe.place(x=480,y=10,width=600,height=80)

        cmb_search=ttk.Combobox(Searchframe,textvariable=self.var_searchby,values=("Select","Category","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(Searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10,width=180)
        btn_search=Button(Searchframe,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=390,y=8,width=100,height=28)

        #tree view---
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(p_frame,columns=("pid","Category","name","qty","price","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("pid",text="Cust.-Id")
        self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("name",text="Product_Name")
        self.ProductTable.heading("qty",text="Quantity")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("status",text="Status")
        
        self.ProductTable['show']="headings"

        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("Category",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        
#=============================================================================
    
    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  

    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_name.set(row[2])
        self.var_price.set(row[4])
        self.var_status.set(row[5])

    
    def delete(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select product from list!",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product !",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully!!",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_cat.set("")
        
        self.var_name.set("")
        
        self.var_price.set("")
        self.var_status.set("")
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option !",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search Input Should br Required !",parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found !",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    

if __name__=="__main__":
    root=Tk()
    obj=proclass(root)
    root.mainloop()