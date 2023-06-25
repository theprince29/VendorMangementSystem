from distutils.command.config import config
from logging import exception
from msilib.schema import ComboBox
from tkinter import*
from tkinter import ttk,messagebox
from turtle import bgpic
from PIL import Image,ImageTk
import sqlite3
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN PAGE")
        self.root.geometry("1080x630+150+30")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        
        # Adding Background----
        self.bg=ImageTk.PhotoImage(file="Images/glacier.jpg")
        bg=Label(self.root,image=self.bg).place(x=380,y=0,width=700,relheight=1)
        # Adding left side image--
        
        self.left=ImageTk.PhotoImage(file="Images/img28.jpeg")
        left=Label(self.root,image=self.left).place(x=0,y=0,width=380,height=630)

        title=Label(self.root,text="LOGIN / SIGN-UP",font=("goudy old style",25,"bold","underline"),bg="light blue",fg="gray").place(x=600,y=23)
        
        l_name=Label(self.root,text="User-Email",font=("times new roman",18,"bold","italic"),bg="white",fg="gray").place(x=660,y=220)
        self.txt_l_name=Entry(self.root,font=("times new roman",15),bg="white")
        self.txt_l_name.place(x=580,y=260,width=300)


        l_password=Label(self.root,text="Password",font=("times new roman",18,"bold","italic"),bg="light blue",fg="gray").place(x=670,y=320)
        self.txt_l_password=Entry(self.root,show="*",font=("times new roman",15),bg="white")
        self.txt_l_password.place(x=580,y=370,width=300)
        #login type================
        
        l_type=Label(self.root,text="Login-Type",font=("times new roman",15,"italic"),bg="light blue",fg="gray").place(x=280,y=2)
        self.txt_l_type=ttk.Combobox(self.root,font=("times new roman",15),values=("Shopkeeper","Dealer","Admin"),state='readonly',justify=CENTER)
        self.txt_l_type.place(x=380,y=2,width=130)
    
        self.txt_remember=Checkbutton(self.root,text="Remember me")
        self.txt_remember.place(x=580,y=410)

        f_password=Button(self.root,text="Forgot Password ?",command=self.forgot,font=("times new roman",10,"italic"),bg="white",fg="gray").place(x=760,y=410)

        self.btn_img=ImageTk.PhotoImage(file="Images/btn12.jpg")
        btn_register=Button(self.root,image=self.btn_img,command=self.login,bd=5,bg="lightblue",cursor="hand2").place(x=660,y=460)

        btn_Registers=Button(self.root,text="Register-Now",command=self.register_window,bg="light blue",font=("times new roman",12,"italic","underline","bold"),bd=0,cursor="hand2",fg="green").place(x=202,y=550)
        note=Label(self.root,text="Do Not Have Account?",font=("times new roman",12,"italic"),bd=0,fg="red").place(x=50,y=550,height=29)
    
    def forgot(self):
        messagebox.showerror("Error","Sorry This Feature is Not Working Right Now!!",parent=self.root)

    def clear(self):
        self.txt_l_name.delete(0,END)
        self.txt_l_password.delete(0,END)
        self.txt_remember.deselect()
        self.txt_l_type.get("Select")
        

    def register_window(self):
        if self.txt_l_type.get()=="Shopkeeper":
            self.root.destroy()
            os.system("python registers.py")
        elif self.txt_l_type.get()=="Dealer":
            self.root.destroy()
            os.system("python Dealer_register.py")
        elif self.txt_l_type.get()=="Admin":
            messagebox.showinfo("Info","Admin is no need to Register himself/herself",parent=self.root)
        else:
            messagebox.showerror("Error","Please Select any Login Type!!",parent=self.root)

    def login(self):
        if self.txt_l_name.get()==""or self.txt_l_password.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        elif self.txt_l_type.get()=="":
            messagebox.showerror("Error","Please Select Login-Type!!",parent=self.root)
        else:
            con=sqlite3.connect(database=r'sms.db')
            cur=con.cursor()
            if self.txt_l_type.get()=="Shopkeeper":

                try:
                    cur.execute("select * from register where email=? and password=?",(self.txt_l_name.get(),self.txt_l_password.get()))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
                        self.clear()
                    else:
                        messagebox.showinfo("Success!","Welcome to Nexus Wholesales Pvt. Ltd",parent=self.root)
                        self.root.destroy()
                        os.system("python shop1.py")
                        #os.system("python customer.py")
                        
                except exception as es:
                    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

            elif self.txt_l_type.get()=="Dealer":
                try:
                    cur.execute("select * from dealer where email=? and password=?",(self.txt_l_name.get(),self.txt_l_password.get()))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
                        self.clear()
                    else:
                        messagebox.showinfo("Success!","Welcome to Nexus Wholesales Pvt. Ltd",parent=self.root)
                        self.root.destroy()
                        os.system("python Dealers_main.py")
                        
                except exception as es:
                    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

            elif self.txt_l_type.get()=="Admin":
                try:
                    if self.txt_l_name.get()!="nexus678@gmail.com"and self.txt_l_password.get()!="Nexus@4562":
                        messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
                        self.clear()
                    elif self.txt_l_name.get()=="nexus678@gmail.com"and self.txt_l_password.get()=="Nexus@4562":
                        messagebox.showinfo("Success!","Welcome to Nexus Wholesales Pvt. Ltd",parent=self.root)
                        self.root.destroy()
                        os.system("python last.py")
                    else:
                        messagebox.showerror("Error","Wrong Input",parent=self.root)
                        
                except exception as es:
                    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

            else:
                messagebox.showerror("Error","Invalid Valid Login-Type!!",parent=self.root)
root=Tk()
obj=Register(root)
root.mainloop()