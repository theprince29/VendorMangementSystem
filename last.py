from logging import root
from re import I, L
from textwrap import fill
from tkinter import*
from PIL import Image,ImageTk
from turtle import title
from tkinter import messagebox
from cust import custclass
from suppl import supplclass
from pro import proclass
from deal import dealer_class
import time
import sqlite3
import os
class SMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1522x783+0+0")
        self.root.title("Shop-Management System")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        # title------
        title=Label(self.root,text="Vendors Management System",font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        # button logout---
        btn_logout=Button(self.root,command=self.log_out,text="Log-Out",font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1300,y=10,height=50,width=150)
        #clock---
        self.lbl_clock=Label(self.root,text="Welcome to Nexus Online Portal\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #Left menu---
        self.menulogo=Image.open("Images/menu_im.png")
        self.menulogo=self.menulogo.resize((200,300),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)

        Leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Leftmenu.place(x=0,y=102,width=200,height=625)

        lbl_menulogo=Label(Leftmenu,image=self.menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.sides_icons=PhotoImage(file="Images/side.png")
        lbl_menu=Label(Leftmenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)

        btn_customer=Button(Leftmenu,text="Customers",command=self.customer,image=self.sides_icons,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_customer=Button(Leftmenu,text="Dealers",command=self.dealer,image=self.sides_icons,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_customer=Button(Leftmenu,text="Supplier",command=self.supplier,image=self.sides_icons,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)       
        btn_customer=Button(Leftmenu,text="Products",command=self.product,image=self.sides_icons,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_customer=Button(Leftmenu,text="Exit",command=self.exit,image=self.sides_icons,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        #body----
        self.lbl_customer=Label(self.root,text="Total Customers\n[0]",bg="#33bbf9",bd=5,relief=GROOVE,fg="white",font=("goudy old style",20,"bold"))
        self.lbl_customer.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]",bg="orange",bd=5,relief=GROOVE,fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_dealer=Label(self.root,text="Total Dealers\n[0]",bg="blue",bd=5,relief=GROOVE,fg="white",font=("goudy old style",20,"bold"))
        self.lbl_dealer.place(x=1000,y=120,height=150,width=300)

        self.lbl_products=Label(self.root,text="Total Products\n[0]",bg="purple",bd=5,relief=GROOVE,fg="white",font=("goudy old style",20,"bold"))
        self.lbl_products.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Placed Orders\n[0]",bg="green",bd=5,relief=GROOVE,fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        # footer----
        lbl_footer=Label(self.root,text="SMS-Shop Management System | Developed by SSMSP\tFor any technical issue contact at Nexustech54@gmail.com",font=("times new roman",13),bg="#4d636d",fg="white").place(x=0,y=720,width=1550,height=70)

        self.update_content()
#--------------------------------------------------------------------------------
    def customer(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=custclass(self.new_win) 

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplclass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=proclass(self.new_win) 

    def dealer(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=dealer_class(self.new_win)

    def exit(self):
        self.root.destroy()

    def log_out(self):
        op=messagebox.askyesno("Confirm","Do you Really want to Log-Out ?",parent=self.root)
        if op==True:
            messagebox.showinfo("Inform","Thanks for Coming to Nexus Shop Management Portal\nHaving a Nice Day",parent=self.root)
            self.root.destroy()
            os.system("python login.py")
        else:
            pass

    def update_content(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_products.config(text=f'Total Products\n[{str(len(product))}]')
            
            cur.execute("select * from supplier")
            Supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(Supplier))}]')

            cur.execute("select * from dealer")
            Category=cur.fetchall()
            self.lbl_dealer.config(text=f'Total Dealers\n[{str(len(Category))}]')

            cur.execute("select * from employee")
            Customer=cur.fetchall()
            self.lbl_customer.config(text=f'Total Customers\n[{str(len(Customer))}]')
            bill=len(os.listdir('Bills'))
            self.lbl_sales.config(text=f'Placed Orders\n[{str(bill)}]')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Nexus Online Portal\t\t Date: {str(date_)}\t\t Time: {str(time_)} ",font=("times new roman",15),bg="#4d636d",fg="white")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=SMS(root)
    root.mainloop()