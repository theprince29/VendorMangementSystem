from ast import Delete
from optparse import Values
import os
import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from turtle import width
from PIL import Image,ImageTk

class Dealer_Registerclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x600+60+50")
        self.root.title("Shop-Management System")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        self.root.focus_force()

        ##------------all variables
       
        self.var_name=StringVar()
        self.var_agency=StringVar()
        self.var_Anygov_id=StringVar()
        self.var_contacts=StringVar()
        self.var_password=StringVar()
        self.var_Id_No=StringVar()
        self.var_email=StringVar()

        # self.cat_list=[]
        # self.sup_list=[]
        # self.fetch_cat_sup()

        ## Title------
        main_frame=Frame(self.root,bg="light yellow",bd=2,relief=RIDGE)
        main_frame.place(x=30,y=10,width=1200,height=550)
        title=Label(self.root,text="Note :-  All Fields Are Required !!",bg="lightyellow",font=("goudy old style",15),fg="red").place(x=580,y=50,width=280)
        title=Label(self.root,text="Dealer Registration Window",bg="#0f4d7d",font=("goudy old style",25),fg="white").place(x=30,y=10,width=1200)

        ##content-----
        #Left menu---
        self.menulogo=Image.open("Images/sales.jpg")
        self.menulogo=self.menulogo.resize((330,500),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)

        lbl_menulogo=Label(main_frame,image=self.menulogo)
        lbl_menulogo.place(x=0,y=42)

        #Row1-----
        lbl_agency=Label(main_frame,text="Agency_Name/Company Name",font=("times new roman",18),bg="light yellow").place(x=400,y=97)
        txt_agency=Entry(main_frame,textvariable=self.var_agency,font=("goudy old style",15),bg="light gray")
        txt_agency.place(x=720,y=100,width=330)

        lbl_password=Label(self.root,text="Create_Password",bg="light yellow",font=("goudy old style",15,"bold")).place(x=800,y=260)
        #lbl_title=Label(self.root,text="Customer Id",bg="white",font=("goudy old style",15)).place(x=50,y=150)
        lbl_name=Label(main_frame,text="Name",bg="light yellow",font=("goudy old style",20)).place(x=400,y=150)
        lbl_contact=Label(main_frame,text="Contact",bg="light yellow",font=("goudy old style",16,"bold")).place(x=800,y=150)
       
        #txt_title=Entry(main_frame,textvariable=self.var_cust_id,bg="white",state='readonly',font=("goudy old style",15)).place(x=160,y=150,width=180)
        txt_name=Entry(main_frame,textvariable=self.var_name,font=("goudy old style",15),bg="light gray")
        txt_name.place(x=550,y=150,width=180)
        
        txt_contact=Entry(main_frame,textvariable=self.var_contacts,font=("goudy old style",15),bg="light gray")
        txt_contact.place(x=875,y=150,width=180)
        
        #User type====
        txt_password=Entry(main_frame,textvariable=self.var_password,justify=CENTER,font=("goudy old style",15),bg="light gray")
        txt_password.place(x=910,y=250,width=180)
        

        #Row2--------
        lbl_email_id=Label(main_frame,text="Email-Id.",bg="light yellow",font=("goudy old style",15,"bold")).place(x=400,y=250)
        lbl_Id_no=Label(main_frame,text="Gov-Id No.",bg="light yellow",font=("goudy old style",15,"bold")).place(x=780,y=200)
        lbl_govid=Label(main_frame,text="Any Gov-Id",bg="light yellow",font=("goudy old style",15,"bold")).place(x=400,y=200)
       
        cmb_gov_id=ttk.Combobox(main_frame,textvariable=self.var_Anygov_id,values=("Select","Aadhar Card","PAN Card","Voter-Id","Any-Other"),state='readonly',justify=CENTER)
        cmb_gov_id.place(x=550,y=200,width=180,height=28)
        cmb_gov_id.current(0)
        txt_email=Entry(main_frame,textvariable=self.var_email,bg="light gray",font=("goudy old style",15)).place(x=550,y=250,width=180)
        txt_govid=Entry(main_frame,textvariable=self.var_Id_No,bg="light gray",font=("goudy old style",15)).place(x=875,y=200,width=180)

        #Row3------
        lbl_address=Label(main_frame,text="Address",font=("times new roman",18),bg="light yellow").place(x=400,y=300)
        self.txt_address=Text(main_frame,bg="lightgray",font=("goudy old style",15))
        self.txt_address.place(x=540,y=300,width=300,height=60)

        

        # Creating terms----
        self.var_chk=IntVar()
        chk=Checkbutton(main_frame,text="I Agree the Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=410,y=380)

        #buttons-----------
        btn_add=Button(main_frame,text="Register Now",command=self.dealer_data,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=630,y=420,width=180,height=35)
        btn_Registers=Button(main_frame,text="Sign-In",bg="light yellow",command=self.login,font=("times new roman",14,"italic","underline","bold"),bd=0,cursor="hand2",fg="green").place(x=810,y=475)
        note=Label(main_frame,text="Already-Registered Dealer ?",font=("times new roman",13,"italic"),bd=0,fg="green").place(x=600,y=480)
#=============================All Functions======================================
    def dealer_data(self):
        if self.var_agency.get()=="" or self.var_name.get()=="" or self.var_email.get()==""or self.var_Anygov_id.get()=="Select"or self.var_Id_No.get()==""or self.var_password.get()==""or self.var_contacts.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Condition",parent=self.root)
        else:
            con=sqlite3.connect(database=r'sms.db')
            cur=con.cursor()
            try:
                cur.execute("select * from dealer where email=?",(self.var_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error"," User Already Exists ? ",parent=self.root)
                else:
                    cur.execute("insert into dealer (agency,name,contact,gov_id,id_no,email,password,address) values(?,?,?,?,?,?,?,?)",
                                    (self.var_agency.get(),
                                    self.var_name.get(),
                                    self.var_contacts.get(),
                                    self.var_Anygov_id.get(),
                                    self.var_Id_No.get(),
                                    self.var_email.get(),
                                    self.var_password.get(),
                                    self.txt_address.get('1.0',END)
                                    ))
                    con.commit()
                    messagebox.showinfo("Success!","Dealer is Succesfully Registered",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def clear(self):
        self.var_agency.set(""),
        self.var_name.set(""),
        self.var_contacts.set(""),
        self.var_Anygov_id.set("Select"),
        self.var_Id_No.set(""),
        self.var_email.set(""),
        self.var_password.set(""),
        self.var_chk.set(""),
        self.txt_address.delete('1.0',END)

    def login(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root=Tk()
    obj=Dealer_Registerclass(root)
    root.mainloop()