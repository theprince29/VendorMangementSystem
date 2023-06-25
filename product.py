from ast import Delete
from cgitb import text
from logging import exception
import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from category import categoryclass

class productclass:
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
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_price=StringVar()
        self.var_name=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        #product frame===
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)

         ## Title------
        title=Label(product_frame,text="Manage Product Details",bg="#0f4d7d",font=("goudy old style",18),fg="white").pack(side=TOP,fill=X)
        
        lbl_category=Label(product_frame,text="Category",bg="white",font=("goudy old style",18)).place(x=30,y=80)
        btn_category=Button(product_frame,text="Manage Categories",command=self.category,bg="white",font=("goudy old style",18)).place(x=150,y=70,width=200,height=28)
        lbl_product=Label(product_frame,text="Product_Name",bg="white",font=("goudy old style",16)).place(x=17,y=160)
        lbl_quantity=Label(product_frame,text="Quantity",bg="white",font=("goudy old style",18)).place(x=30,y=210)
        lbl_price=Label(product_frame,text="Price",bg="white",font=("goudy old style",18)).place(x=30,y=260)
        lbl_status=Label(product_frame,text="Status",bg="white",font=("goudy old style",18)).place(x=30,y=310)

        #====options======
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=100,width=200)
        cmb_cat.current(0)

        # cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        # cmb_sup.place(x=150,y=112,width=200)
        # cmb_sup.current(0)
        self.txt_dealer_name=StringVar()
        lbl_deal_name=Label(product_frame,text="Mention your Name",bg="white",font=("goudy old style",13)).place(x=0,y=32,width=150)
        txt_deal_name=Entry(product_frame,textvariable=self.txt_dealer_name,font=("goudy old style",15),bg="light gray",justify=CENTER).place(x=145,y=33,width=180)
        btn_verify=Button(product_frame,text="Verify(At once)",command=self.veify,font=("goudy old style",13),bg="light green",fg="white",cursor="hand2").place(x=326,y=33,width=120,height=25)


        txt_name=Entry(product_frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=160,width=200)
        txt_qty=Entry(product_frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=150,y=210,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=150,y=260,width=200)
        
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Select","Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)

        #buttons-----------
        btn_add=Button(product_frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)

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
        # self.ProductTable.heading("Supplier",text="Supplier")
        self.ProductTable.heading("name",text="Product_Name")
        self.ProductTable.heading("qty",text="Price")
        self.ProductTable.heading("price",text="Quantity")
        self.ProductTable.heading("status",text="Status")
        
        self.ProductTable['show']="headings"

        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("Category",width=100)
        #self.ProductTable.column("Supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        
#=============================================================================
    def veify(self):
        if self.txt_dealer_name.get()=="":
            messagebox.showerror("Error","Please provide your name!!",parent=self.root)
        else:
            con=sqlite3.connect(database=r'sms.db')
            cur=con.cursor()
            try:
                    cur.execute("select * from dealer where name=?",(self.txt_dealer_name.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid Name Verification Failed!!",parent=self.root)
                        
                    else:
                        messagebox.showinfo("confirm","Congratulation You are Verified succesfuly!!",parent=self.root)     
                        pass
            except exception as es:
                    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            # cur.execute("SELECT name from supplier")
            # sup=cur.fetchall()
            # if len(sup)>0:
            #     del self.sup_list[:]
            #     self.sup_list.append("Select")
            #     for j in sup:
            #         self.sup_list.append(j[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def add(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select"or self.var_cat.get()=="Empty"or self.var_sup.get()=="Select"or self.var_name.get()=="":
                messagebox.showerror("Error","All Fields Are Required!",parent=self.root)
            elif self.txt_dealer_name.get()=="":
                messagebox.showerror("Error","Please Mention your name\n It is required only one time!",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","This Product is Alredy Present !",parent=self.root)
                else:
                    cur.execute("Insert into product (Category,name,qty,price,status,dealer_name) values(?,?,?,?,?,?)",
                        (self.var_cat.get(),
                        #self.var_sup.get(),
                        self.var_name.get(),
                        self.var_qty.get(),
                        self.var_price.get(),
                        self.var_status.get(),
                        self.txt_dealer_name.get()
                        ))

                    con.commit()
                    messagebox.showinfo("Success!","Product Added Succesfully!!",parent=self.root)
                 
                self.show()       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

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
        #self.var_sup.set(row[2])
        self.var_name.set(row[2])
        self.var_qty.set(row[4])
        self.var_price.set(row[3])
        self.var_status.set(row[5])

    def update(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product From List!",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid Product !",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,name=?,qty=?,price=?,status=? where pid=?",
                        (
                        self.var_cat.get(),
                        #self.var_sup.get(),
                        self.var_name.get(),
                        self.var_qty.get(),
                        self.var_price.get(),
                        self.var_status.get(),
                        self.var_pid.get()
                        ))

                con.commit()
                messagebox.showinfo("Success!","Product is Succesfully Updated!!",parent=self.root) 
                self.show()       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

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
        self.var_cat.set("Select")
        #self.var_sup.set("Select")
        self.var_name.set("")
        self.var_qty.set("")
        self.var_price.set("")
        self.var_status.set("Select")
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

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=productclass(root)
    root.mainloop()