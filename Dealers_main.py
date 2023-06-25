from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
from dealer_info import Dealer_infoclass
from supplier import supplierclass
from product import productclass
#from select_dealer import searchclass
import sqlite3
import time
import os
class Dealerclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x600+60+50")
        self.root.title("Shop-Management System")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        self.root.focus_force()

        title=Label(self.root,text="Dealers Management System",font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        # button logout---
        btn_logout=Button(self.root,text="Log-Out",command=self.log_out,font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1070,y=10,height=50,width=120)
        #clock---
        self.lbl_clock=Label(self.root,text="Welcome to Nexus Online Portal\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #Left menu---
        self.menulogo=Image.open("Images/cat2.jpg")
        self.menulogo=self.menulogo.resize((200,200),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)

        Leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Leftmenu.place(x=0,y=102,width=230,height=470)

        lbl_menulogo=Label(Leftmenu,image=self.menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.sides_icons=PhotoImage(file="Images/side.png")
        lbl_menu=Label(Leftmenu,text="Menu",font=("times new roman",22),bg="#009688").pack(side=TOP,fill=X)

        btn_customer=Button(Leftmenu,text="Dealer-Info",command=self.dealer_info,image=self.sides_icons,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_customer=Button(Leftmenu,text="Supplier",command=self.supplier,image=self.sides_icons,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_customer=Button(Leftmenu,text="Product",command=self.product,image=self.sides_icons,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_customer=Button(Leftmenu,text="Exit",command=self.exit,image=self.sides_icons,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        self.lbl_supplier=Label(self.root,text="Total Suppliers\n[0]",bg="#33bbf9",bd=5,relief=GROOVE,fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=300,y=150,height=150,width=300)

        self.lbl_products=Label(self.root,text="Total Products\n[0]",bg="orange",bd=5,relief=GROOVE,fg="white",font=("goudy old style",20,"bold"))
        self.lbl_products.place(x=750,y=150,height=150,width=300)

        # footer----
        lbl_footer=Label(self.root,text="SMS-Shop Management System | Developed by SSMSP\tFor any technical issue contact at Nexustech54@gmail.com",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

        self.update_content()
#================================Functions======================================
    def dealer_info(self):
        self.new_win=Toplevel(self.root)
        #self.new_obj=searchclass(self.new_win)
        self.new_obj=Dealer_infoclass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win) 

    def update_content(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            Supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(Supplier))}]')

            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_products.config(text=f'Total Products\n[{str(len(product))}]')            
            
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Nexus Online Portal\t\t Date: {str(date_)}\t\t Time: {str(time_)} ",font=("times new roman",15),bg="#4d636d",fg="white")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def log_out(self):
        op=messagebox.askyesno("Confirm","Do you Really want to Log-Out ?",parent=self.root)
        if op==True:
            messagebox.showinfo("Inform","Thanks for Coming to Nexus Shop Management Portal\nHaving a Nice Day",parent=self.root)
            self.root.destroy()
            os.system("python login.py")
        else:
            pass
    def exit(self):
        self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj=Dealerclass(root)
    root.mainloop()