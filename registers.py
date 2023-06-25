from tkinter import*
from tkinter import ttk,messagebox
from tkinter import messagebox as mb
from PIL import Image,ImageTk
import qrcode
from resizeimage import resizeimage
import sqlite3
import os
import random
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        
        self.var_number=(random.randint(1000,50000))
        # Adding Background----
        self.bg=ImageTk.PhotoImage(file="Images/bg4.webp")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        logo=Label(self.root,text="Welcome To Nexus Shop-Registration Portal",font=("times new roman",25,"italic"),fg="blue").place(x=380,y=90)
        # Adding left side image--
        
        self.left=ImageTk.PhotoImage(file="Images/img4.jpg")
        left=Label(self.root,image=self.left).place(x=30,y=140,width=350,height=520)
        # Assinging variables----
        self.var_f_Name=StringVar()
        self.var_Shop_name=StringVar()
        self.var_Email=StringVar()
        self.var_S_license=StringVar()
        self.var_Contact=StringVar()
        # Creating Frame---
        frame1=Frame(self.root,bg="light yellow")
        frame1.place(x=380,y=140,width=750,height=520)

        # Creating first centered text--
        title=Label(frame1,text="REGISTER YOUR SHOP",font=("times new roman",20,"bold"),bg="White",fg="green").place(x=250,y=30)
        # Creating Row 1---->
        
        f_name=Label(frame1,text="User Name",font=("times new roman",15,"bold"),bg="White",fg="gray").place(x=80,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),textvariable=self.var_f_Name,bg="lightgray")
        self.txt_fname.place(x=80,y=130,width=250)
       
        shop_name=Label(frame1,text="Shop Name",font=("times new roman",15,"bold"),bg="White",fg="gray").place(x=380,y=100)
        self.txt_shopname=Entry(frame1,font=("times new roman",15),textvariable=self.var_Shop_name,bg="lightgray")
        self.txt_shopname.place(x=380,y=130,width=250)
       
        # Creating Row 2----->
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="White",fg="gray").place(x=80,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),textvariable=self.var_Contact,bg="lightgray")
        self.txt_contact.place(x=80,y=200,width=250)
       
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="White",fg="gray").place(x=380,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),textvariable=self.var_Email,bg="lightgray")
        self.txt_email.place(x=380,y=200,width=250)
        
        # Creating Row 3----->
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="White",fg="gray").place(x=80,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First School","Your Favourite Sports","Your Birth Place","Your Pet Name")
        self.cmb_quest.place(x=80,y=270,width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1,text="Security Answer",font=("times new roman",15,"bold"),bg="White",fg="gray").place(x=380,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=380,y=270,width=250)

        # Creating Row 4------>
        password=Label(frame1,text="Create Password",font=("times new roman",15,"bold"),bg="White",fg="gray").place(x=80,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=80,y=340,width=250)
       
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="White",fg="gray").place(x=380,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=380,y=340,width=250)
        
        s_license=Label(frame1,text="Enter Shop Registration/License No.",font=("times new roman",15,"bold"),bg="White",fg="gray").place(x=200,y=380)
        self.txt_slicense=Entry(frame1,font=("times new roman",15),textvariable=self.var_S_license,bg="lightgray")
        self.txt_slicense.place(x=203,y=410,width=303)

        # creating Qr-Code window-----
        qr_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_frame.place(x=1135,y=310,width=208,height=350)
        
        emp_title=Label(qr_frame,text="Registered Shop Unique-QR",font=("goudy old style",13,"bold"),bg="blue",fg="white").place(x=0,y=0)
        mp_title=Label(qr_frame,text="You can also Generate\n your Personalised QR here\n By clicking on Generate Button",font=("times new roman",10,"bold","italic"),bg="white",fg="green").place(x=0,y=35)

        self.qr_Code=Label(qr_frame,text="No QR\nAvailable",font=("times new roman",15),bg='lightblue',fg='white',bd=1,relief=RIDGE)
        self.qr_Code.place(x=12,y=100,width=180,height=180)
        
        # Creating terms----
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree the Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=80,y=440)
        # Creating buttons-----
        self.btn_img=ImageTk.PhotoImage(file="Images/btn10.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,bg="white",cursor="hand2",command=self.register_data).place(x=245,y=472)
        
        btn_login=Button(self.root,text="Sign-In",bg="red",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=158,y=495)
        note=Label(self.root,text="Already-Registered Shop ?",font=("times new roman",13,"italic"),bd=0,fg="green").place(x=120,y=550)

        # <----- creating qr button ------>
        btn_Generate=Button(qr_frame,text=" DELETE-QR ",command=self.delete,font=("times new roman",15),bd=3,bg="green",fg="white",cursor="hand2").place(x=30,y=290)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_shopname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_slicense.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)
        self.var_chk.set('')
        

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()==""or self.cmb_quest.get()=="Select"or self.txt_answer.get()==""or self.txt_password.get()==""or self.txt_cpassword.get()==""or self.txt_contact.get()==""or self.txt_slicense.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error","Password And Confirm Password Is Not same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Condition",parent=self.root)
        else:
            con=sqlite3.connect(database=r'sms.db')
            cur=con.cursor()
            try:
                cur.execute("select * from register where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error"," User Already Exists ? ",parent=self.root)
                else:
                    cur.execute("insert into register (f_name,shop_name,contact,email,question,answer,password,license,cust_Id) values(?,?,?,?,?,?,?,?,?)",
                                    (self.txt_fname.get(),
                                    self.txt_shopname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get(),
                                    self.txt_slicense.get(),
                                    self.var_number
                                    ))
                    con.commit()
                    messagebox.showinfo("Success!","Shop is Succesfully Registered",parent=self.root)
                    op=messagebox.askyesno("Confirm","Do you Want to Generate your Personalised QR Also",parent=self.root)
                    if op==True:
                        self.generate()
                    else:
                        pass
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def generate(self):
        if self.txt_fname.get()=="" or self.txt_email.get()==""or self.cmb_quest.get()=="Select"or self.txt_answer.get()==""or self.txt_password.get()==""or self.txt_cpassword.get()==""or self.txt_contact.get()==""or self.txt_slicense.get()=="":
             messagebox.showerror("Error","User is not Registered Yet!",parent=self.root)
        else:
            qr_data=(f"Customer_Id. : {self.var_number}\nUser-Name : {self.var_f_Name.get()}\nShop-Name : {self.var_Shop_name.get()}\nContact : {self.var_Contact.get()}\nEmail : {self.var_Email.get()}\nShop-License_No. : {self.var_S_license.get()}")
            qr_Code=qrcode.make(qr_data)
            qr_Code=resizeimage.resize_cover(qr_Code,[180,180])
            qr_Code.save("Shop_QR/user_"+str(self.var_f_Name.get())+'.png')
            self.sm=ImageTk.PhotoImage(file="Shop_QR/user_"+str(self.var_f_Name.get())+'.png')
            self.qr_Code.config(image=self.sm)
            messagebox.showinfo("Success!","QR-GENERATED SUCCESSFULLY!!",parent=self.root)

    def delete(self):
        self.qr_Code.config(image='')        
            
                          
root=Tk()
obj=Register(root)
root.mainloop()