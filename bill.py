from logging import root
from operator import index
from tkinter import*
from tkinter import ttk,messagebox
from tkinter import font
from unicodedata import name
from PIL import Image,ImageTk
import random
import sqlite3
import time
import os
import tempfile
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1522x783+0+0")
        self.root.title("Shop-Management System")
        self.root.config(bg="White")
        self.root.resizable(False,False)

        self.cart_list=[]
        self.chk_print=0
        # title------
        tilte_frame1=Frame(self.root,bd=2,relief=RIDGE,bg="#010c48")
        tilte_frame1.place(x=0,y=0,width=1522,height=95)

        title=Label(tilte_frame1,text="Nexus",font=("goudy old style",60,"bold","italic"),bg="#010c48",fg="white").place(x=40,y=0,width=300,height=60)
        title1=Label(tilte_frame1,text="आपका एकमात्र साथी",font=("times new roman",12,"italic"),bg="#010c48",fg="yellow").place(x=290,y=45,width=200,height=25)

        # button logo---
        self.bg=ImageTk.PhotoImage(file="Images/logo1.png")
        bg=Label(tilte_frame1,image=self.bg,bg="#010c48").place(x=1,y=8,height=50)
        #clock---
        self.lbl_clock=Label(self.root,text="Welcome to Vendors Management Portal\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        # button logout---
        btn_logout=Button(tilte_frame1,text="Log-Out",command=self.log_out,font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1350,y=10,height=40,width=120)
        #==Product frame===
        
        Productframe1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Productframe1.place(x=6,y=110,width=440,height=630)

        pTitle=Label(Productframe1,text="All Products",font=("times new roman",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        #==product search frame====
        self.var_search=StringVar()

        Productframe2=Frame(Productframe1,bd=2,relief=RIDGE,bg="white")
        Productframe2.place(x=2,y=42,width=428,height=130)

        lbl_search=Label(Productframe2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search=Label(Productframe2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=90)
        txt_search=Entry(Productframe2,textvariable=self.var_search,font=("times new roman",15,"bold"),bg="lightyellow").place(x=129,y=92,width=150,height=30)
        btn_search=Button(Productframe2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=284,y=92,width=130,height=30)
        btn_show_all=Button(Productframe2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=284,y=10,width=130,height=25)

        #tree view of product frame--------
        Productframe3=Frame(Productframe1,bd=3,relief=RIDGE)
        Productframe3.place(x=2,y=175,width=425,height=420)

        scrolly=Scrollbar(Productframe3,orient=VERTICAL)
        scrollx=Scrollbar(Productframe3,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(Productframe3,columns=("pid","Category","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        self.product_table.heading("pid",text="PID")
        self.product_table.heading("Category",text="Category")
        self.product_table.heading("name",text="P_Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="Qty.")
        self.product_table.heading("status",text="Status")
       

        self.product_table['show']="headings"

        self.product_table.column("pid",width=40)
        self.product_table.column("Category",width=100)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status",width=80)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(Productframe1,text="Note : 'Enter 0 to Remove Product from cart' ",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #=====customer frame===========================
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        Customerframe=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Customerframe.place(x=450,y=110,width=560,height=120)

        cTitle=Label(Customerframe,text="Customer Details",font=("times new roman",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(Customerframe,text="Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=55)
        txt_name=Entry(Customerframe,textvariable=self.var_cname,font=("times new roman",13,"bold"),bg="lightyellow").place(x=80,y=55,width=180)

        lbl_contact=Label(Customerframe,text="Contact",font=("times new roman",15,"bold"),bg="white").place(x=275,y=55)
        txt_contact=Entry(Customerframe,textvariable=self.var_contact,font=("times new roman",13,"bold"),bg="lightyellow").place(x=360,y=55,width=155)

        Cartframe=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cartframe.place(x=450,y=250,width=560,height=360)

        Cal_frame=Frame(Cartframe,bd=3,relief=RIDGE,bg="white")
        Cal_frame.place(x=5,y=85,width=268,height=250)

        #tree view of customer frame-------
        cart_frame=Frame(Cartframe,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=265,height=342)

        self.cartTitle=Label(cart_frame,text="Cart \t Total Products: [0]",font=("times new roman",15),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_frame,columns=("pid","name","price","qty","type"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="Quantity")
        self.CartTable.heading("type",text="P_Type")
        
       
        self.CartTable['show']="headings"

        self.CartTable.column("pid",width=50)
        self.CartTable.column("name",width=90)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=100)
        self.CartTable.column("type",width=70)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)

        #add cart button=========================
        self.var_pid=StringVar()
        self.var_pName=StringVar()
        self.var_type=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_stock=StringVar()
        self.var_price=StringVar()

        add_Cartframe=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        add_Cartframe.place(x=450,y=630,width=560,height=110)

        lbl_p_name=Label(add_Cartframe,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(add_Cartframe,textvariable=self.var_pName,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_type=Label(add_Cartframe,text="Price Per Qty.",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_type=Entry(add_Cartframe,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lbl_p_qty=Label(add_Cartframe,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(add_Cartframe,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=150,height=22)
        
        self.lbl_instock=Label(add_Cartframe,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_instock.place(x=5,y=70)

        btn_clear=Button(add_Cartframe,text="Clear",command=self.clear_cart,font=("goudy old style",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_addcart=Button(add_Cartframe,text="Add | Update Cart",command=self.add_update_cart,font=("goudy old style",15,"bold"),bg="orange",cursor="hand2").place(x=350,y=70,width=180,height=30)

        #selection window=====================
        self.var_dealer=StringVar()
        self.var_suppl=StringVar()
        self.dealer_list=[]
        self.sup_list=[]
        self.fetch_dealer()

        lbl_dealer=Label(Productframe2,text="Select Dealer",font=("goudy old style",17,"bold"),bg="white",fg="blue").place(x=5,y=45)
        self.cmb_deal=ttk.Combobox(Productframe2,textvariable=self.var_dealer,values=self.dealer_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        self.cmb_deal.place(x=129,y=47,width=150,height=30)
        self.cmb_deal.current(0)

        

        lbl_supplier=Label(Cartframe,text="Select Supplier",font=("goudy old style",15,"bold"),bg="white",fg="blue").place(x=75,y=10)
        self.cmb_suppl=ttk.Combobox(Cartframe,textvariable=self.var_suppl,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        self.cmb_suppl.place(x=40,y=36,width=170,height=30)
        self.cmb_suppl.current(0)
        btn_supll=Button(Cartframe,text="GO",command=self.select_supplier,font=("goudy old style",15,"bold"),bg="lightgray",cursor="hand2").place(x=210,y=36,width=50,height=28)


        btn_clear=Button(Productframe2,text="Proceed",command=self.select_dealer,font=("goudy old style",15,"bold"),bg="lightgray",cursor="hand2").place(x=284,y=45,width=130,height=30)

    #==========================================================================
        self.var_sid=StringVar()
        self.var_sname=StringVar()
        self.var_scontact=StringVar()
        self.var_adrs=StringVar()  

    #=========================
        sup_frame=Frame(Cal_frame,bd=3,relief=RIDGE)
        sup_frame.place(x=0,y=0,width=260,height=70)

        # self.cartTitle=Label(sup_frame,text="Cart \t Total Products: [0]",font=("times new roman",15),bg="lightgray")
        # self.cartTitle.pack(side=TOP,fill=X)

        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.SupTable=ttk.Treeview(sup_frame,columns=("sid","name","contact","adrs"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        #scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupTable.xview)
        scrolly.config(command=self.SupTable.yview)
        self.SupTable.heading("sid",text="SID")
        self.SupTable.heading("name",text="Name")
        self.SupTable.heading("contact",text="Contact")
        #self.SupTable.heading("adrs",text="")

        self.SupTable['show']="headings"

        self.SupTable.column("sid",width=30)
        self.SupTable.column("name",width=90)
        self.SupTable.column("contact",width=120)
        #self.SupTable.column("adrs",width=90)
        self.SupTable.pack(fill=BOTH,expand=1)
        self.SupTable.bind("<ButtonRelease-1>",self.get_datasup)

        #lbl_p_supcon=Label(Cartframe,text="Contact",font=("times new roman",15),bg="white").place(x=100,y=100)
        txt_p_supcon=Entry(Cartframe,state="readonly",textvariable=self.var_scontact,font=("times new roman",15),bg="lightyellow").place(x=50,y=400,width=80,height=30)
        lbl_desc=Label(Cartframe,text="Supplier_Add.",font=("times new roman",15),bg="white").place(x=90,y=180)
        txt_Supdesc=Entry(Cartframe,bg="lightyellow",state="readonly",textvariable=self.var_adrs,font=("goudy old style",15))
        txt_Supdesc.place(x=20,y=210,width=240,height=80)


        #=================Bill Area==========================
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=1013,y=110,width=500,height=490)

        bTitle=Label(billFrame,text="Customer Billing Area",font=("times new roman",20,"bold"),bg="red",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        #===Bill Buttons===========
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=1013,y=607,width=500,height=135)

        self.lbl_amnt=Label(billMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=150,height=70)

        self.lbl_discount=Label(billMenuFrame,text="Discount\n[0%]",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=155,y=5,width=150,height=70)

        self.lbl_netpay=Label(billMenuFrame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_netpay.place(x=310,y=5,width=180,height=70)

        btn_print=Button(billMenuFrame,text="Generate Bill",command=self.generate_bill,font=("goudy old style",15,"bold"),bg="blue",fg="white",cursor="hand2")
        btn_print.place(x=2,y=80,width=150,height=50)

        btn_Clear=Button(billMenuFrame,text="Clear All",command=self.clear_all,font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2")
        btn_Clear.place(x=155,y=80,width=152,height=50)

        btn_order=Button(billMenuFrame,text="Place Order",command=self.print_bill,font=("goudy old style",15,"bold"),bg="#009688",fg="white",cursor="hand2")
        btn_order.place(x=310,y=80,width=180,height=50)
        
        #footer====================
        footer=Label(self.root,text="Vendors Management System | Developed by Nexus Pvt. Ltd\nFor any Issue Regarding this Contact Tech. Assistant",font=("times new roman",11),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.show_sup()
        self.show()
        self.update_datetime()        
#=====================All Functions=============================================
    def select_dealer(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.cmb_deal.get()=="Select":
                messagebox.showerror("Error","Please Select any Dealer",parent=self.root)
            else:
                cur.execute("select * from product where dealer_name =?",(self.cmb_deal.get(),))
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found !",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def fetch_dealer(self):
        self.dealer_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT name from dealer")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.dealer_list[:]
                self.dealer_list.append("Select")
                for i in cat:
                    self.dealer_list.append(i[0])
            
            cur.execute("select name from supplier where name LIKE '%"+"%' and status='Active'")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for j in sup:
                    self.sup_list.append(j[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("Select pid,Category,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  


    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search Input Should br Required !",parent=self.root)
            else:
                cur.execute("select * from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found !",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pName.set(row[2])
        self.var_type.set(row[1])
        self.var_price.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        self.var_qty.set('1')

    #("pid","name","price","qty","type")
    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pName.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.var_type.set(row[4])
        self.var_stock.set(row[5])
        self.lbl_instock.config(text=f"In Stock [{str(row[5])}]")
        
       # ("pid","name","price","qty","type")
    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror("Error","Please select product from list !!",parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror("Error","Please Enter Quantity !!",parent=self.root)        
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity !!",parent=self.root)  

        else:
            cart_data=[self.var_pid.get(),self.var_pName.get(),self.var_price.get(),self.var_qty.get(),self.var_type.get(),self.var_stock.get()]
            #update cart====
            present='no'
            index=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index +=1
            if present=='yes':
                op=messagebox.askyesno("Confirm","Product Already Present\nDo you want to Update|Remove from cart",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index)
                    else:
                        self.cart_list[index][3]=self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()
    def bill_updates(self):
        self.number=(random.randint(0,6))

        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[3])*int(row[2]))

        self.discount=(self.bill_amnt*(self.number))/100
        self.net_pay=self.bill_amnt-self.discount
        self.lbl_amnt.config(text=f'Bill Amnt.(Rs.)\n[{str(self.bill_amnt)}]')
        self.lbl_netpay.config(text=f'Net Pay(Rs.)\n[{str(self.net_pay)}]')
        self.lbl_discount.config(text=f'Discount(%) \n[{str(self.number)}]')

        self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")


    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  


    def generate_bill(self):
        if self.var_cname.get()==''or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are Required",parent=self.root)
        elif len(self.cart_list)<=0:
            messagebox.showerror("Error","Please Add Product to Cart",parent=self.root)
        else:
            #Bill Top===
            self.bill_top()
            #Bill Middle===
            self.bill_middle()
            #Bill Bottom===
            self.bill_bottom()

            fp=open(f'Bills/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved","Bill has been Generated!!!",parent=self.root)
            self.chk_print=1

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\t\tNexus-Shopping Portal
\t\t Phone No. 98725***** , Delhi-125001
{str("="*58)}
 Customer Name: {self.var_cname.get()}
 Phone NO. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}

 Dealer-Name : {str(self.cmb_deal.get())}
 Supplier : {str(self.cmb_suppl.get())}
 Supplier_Contact : {str(self.var_scontact.get())}
{str("="*58)}
 Product Name\t\t\tQTY\t  Price
{str("="*58)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*58)}
 Bill Amount\t\t\t\tRs.  {self.bill_amnt}
 Discount\t\t\t\tRs.  {self.discount}
 Net Pay\t\t\t\tRs.  {self.net_pay}
{str("="*58)}\n
      Thanks For Doing Shopping with us!
             Have a nice Day!!!
{str("="*58)}
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)

    def bill_middle(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:            # ("pid","name","price","qty","type")
            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=int(row[5])-int(row[3])
                qty=str(qty)
                if int(row[3])==int(row[5]):
                    status='Inactive'
                if int(row[3])!=int(row[5]):
                    status='Active'
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\t Rs."+price)
            #=========update product backend======
                cur.execute('Update product set qty=?,status=? where pid=?',(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pName.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.var_type.set('')
        self.var_stock.set('')
        self.lbl_instock.config(text=f"In Stock")
        
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.clear_cart()
        self.show()
        self.show_cart()
        self.var_search.set('')
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.chk_print=0
        self.bill_updates()
        self.cmb_deal.set('Select')
        self.cmb_suppl.set('Select')
        self.var_adrs.set('')

    def update_datetime(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Vendors Management Portal\t\t Date: {str(date_)}\t\t Time: {str(time_)} ",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.after(200,self.update_datetime)
    
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Success","Order Placed Successfully\nThanks for Shopping Have a Nice Day!!",parent=self.root)
            messagebox.showinfo("Print","Please wait while Printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Error","Please Generate bill !",parent=self.root)

    def show_sup(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("Select invoice,name,contact,desc from supplier where status='Active'")
            rows=cur.fetchall()
            self.SupTable.delete(*self.SupTable.get_children())
            for row in rows:
                self.SupTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)  

    def get_datasup(self,ev):
        f=self.SupTable.focus()
        content=(self.SupTable.item(f))
        row=content['values']
        self.var_adrs.set(row[3])
        self.var_scontact.set(row[2])
        # self.txt_Supdesc.delete('1.0',END)
        # self.txt_Supdesc.insert(END,row[3])    

    def select_supplier(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.cmb_suppl.get()=="Select":
                messagebox.showerror("Error","Please Select any Supplier",parent=self.root)
            else:
                cur.execute("select * from supplier where name =?",(self.cmb_suppl.get(),))
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.SupTable.delete(*self.SupTable.get_children())
                    for row in rows:
                        self.SupTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found !",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def log_out(self):
        op=messagebox.askyesno("Confirm","Do you Really want to Log-Out ?",parent=self.root)
        if op==True:
            messagebox.showinfo("Inform","Thanks for Coming to Nexus Shop Management Portal\nHave a Nice Day",parent=self.root)
            self.root.destroy()
            os.system("python shop1.py")
        else:
            pass


if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()